from medicine.views import medicineForUser
import datetime
from level.serializers import LevelSerializer
from step.serializers import StepForUserSerializer,StepSerializer
from level.models import Level
from .models import  StepForUser,Step
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

#------------------------------- for admin ----------------------------------#
@api_view(['POST'])
def InsertStep(request):
    serializer = StepSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def updateStep(request):
    if request.method == 'PUT':
        try:
            step = Step.objects.get(levelNumber=request.data.get('levelNumber'),stepNumber=request.data.get('stepNumber'))
        except Step.DoesNotExist:
            return Response('')
        serializer = StepSerializer(step, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    
@api_view(['GET'])
def getAllSteps(request):
    steps = Step.objects.all()
    serializer = StepSerializer(steps, many=True)
    return Response(serializer.data)
    
@api_view(['DELETE'])
def deleteStep(request):
    try:
        step = Step.objects.get(levelNumber=request.data.get('levelNumber'),stepNumber=request.data.get('stepNumber'))
    except Step.DoesNotExist:
        return Response({'message': 'ERROR'})
    step.delete()
    return Response({'message': 'deleted successfuly'})


#------------------------------- for user ----------------------------------#

@api_view(['POST'])
def delaySteps(request):
    mail=request.data.get('mail')
    newDate=buildDate(request.data.get('date'))
    day=getDelay(newDate)
    allStepOfuser=sortSteps(StepForUser.objects.filter(mail=mail))
    currentStep=list(filter(lambda x:x.isCurrStep==True,allStepOfuser))[0]
    index=allStepOfuser.index(currentStep)
    for sfu in allStepOfuser[index+1:]:
        sfu.date+=datetime.timedelta(days=day)
        sfu.save()
   
    timeLine=path(mail)
    return Response(timeLine)

@api_view(['POST'])
def getPath(request):
    mail=request.data.get('mail')
    timeLine=path(mail)
    return Response(timeLine)

@api_view(['GET'])
def getNameSteps(request):
    names=[]
    for step in Step.objects.all():
        names.append("שלב {0} תחנה {1}".format(step.levelNumber,step.stepNumber))
    return Response(names)


@api_view(['POST'])
def next(request):
    mail=request.data.get('mail')
    levelNumber=request.data.get('levelNumber')
    stepNumber=request.data.get('stepNumber')
    isNextLevel=request.data.get('isNextLevel')

    if isNextLevel:
        nextLevel=int(request.data.get('nextLevel'))
        medicineForUser(mail,nextLevel)

    newStep=StepForUser.objects.get(mail=mail,levelNumber=levelNumber,stepNumber=stepNumber)
    newStep.isCurrStep=True
    newStep.save()

    
    oldStep=list(filter(lambda x:x.isCurrStep==True,StepForUser.objects.filter(mail=mail)))[0]
    oldStep.isDone=True
    oldStep.isCurrStep=False
    oldStep.save()
    timeLine=path(mail)
    return Response(timeLine)

@api_view(['POST'])
def back(request):
    mail=request.data.get('mail')
    levelNumber=request.data.get('levelNumber')
    stepNumber=request.data.get('stepNumber')
    isBackLevel=request.data.get('isBackLevel')
    if isBackLevel:
        backLevel=int(request.data.get('backLevel'))
        medicineForUser(mail,backLevel) 
        
    oldStep=list(filter(lambda x:x.isCurrStep==True,StepForUser.objects.filter(mail=mail)))[0]
    oldStep.isCurrStep=False
    oldStep.save()

    newStep=StepForUser.objects.get(mail=mail,levelNumber=levelNumber,stepNumber=stepNumber)
    newStep.isCurrStep=True
    newStep.isDone=False
    newStep.save()

    
    timeLine=path(mail)
    return Response(timeLine)

#------------------------------- help functions ----------------------------------#
def path(mail):
    
    allStep=StepForUser.objects.filter(mail=mail)
    currlevel=list(filter(lambda x:x.isCurrStep==True,allStep))[0].levelNumber
    
    allLevel=Level.objects.all().order_by('levelNumber')
   
    timeLine=[]
    for level in allLevel:
        levelsir=LevelSerializer(level).data
        if level.levelNumber <= currlevel:
            levelsir['isDone']=True
        else:
            levelsir['isDone']=False
        tempLevel=[levelsir,]
        stepOfLevel=allStep.filter(levelNumber=level.levelNumber).order_by("stepNumber")
        stepsOfLevelSir=StepForUserSerializer(stepOfLevel,many=True)
        tempLevel+=stepsOfLevelSir.data
        timeLine.append(tempLevel)
        
    return timeLine   
def stepForUser(user):
    allSteps=sortSteps(Step.objects.all())
    stepInFirstLevel=list(filter(lambda x:x.levelNumber==1, allSteps))
    firstStep=min(stepInFirstLevel,key=lambda x:x.stepNumber)
    currlevel=1
    lastDate=datetime.datetime.now()
    lastStepNumber=0
    for step in allSteps:
        sfu=StepForUser(mail=user['mail'],
                        levelNumber=step.levelNumber,
                        stepNumber=step.stepNumber,
                        description=step.description,
                        requirements=step.requirements)

        if sfu.levelNumber == 1 and sfu.stepNumber ==firstStep.stepNumber :
            sfu.isCurrStep=True

        if sfu.levelNumber==currlevel:
            sfu.date=lastDate+datetime.timedelta(days=sfu.stepNumber-lastStepNumber)
            lastDate=sfu.date
            lastStepNumber=sfu.stepNumber
        else:
            sfu.date=lastDate+datetime.timedelta(days=sfu.stepNumber)
            lastDate=sfu.date
            lastStepNumber=sfu.stepNumber
            currlevel=sfu.levelNumber
        sfu.save()

def sortSteps(allSteps):
    countLevels=max(allSteps,key=lambda x:x.levelNumber).levelNumber
    sorted=[]
    for level in range(1,countLevels+1):
       temp=(list(filter(lambda x:x.levelNumber==level,allSteps)))
       temp.sort(key=lambda x:x.stepNumber)
       
       sorted+=temp
    return sorted
def getDelay(newDate):
    delta=(newDate-datetime.datetime.now())
    return delta.days
def buildDate(newDate):
    return datetime.datetime(newDate["year"],newDate["month"],newDate["day"])