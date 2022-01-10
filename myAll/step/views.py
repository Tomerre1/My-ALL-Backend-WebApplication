from re import T
from django.shortcuts import render
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
def getPath(request):
    mail=request.data.get('mail')
    timeLine=path(mail)
    return Response(timeLine)

@api_view(['POST'])
def next(request):
    mail=request.data.get('mail')
    levelNumber=request.data.get('levelNumber')
    stepNumber=request.data.get('stepNumber')
    isNextLevel=request.data.get('isNextLevel')
    if isNextLevel:
        nextLevel=int(request.data.get('nextLevel'))
        try:
            oldLevel=Level.objects.get(levelNumber=(nextLevel-1))
        except Level.DoesNotExist:
            return Response('')
        # oldLevel.isDone=True
        # oldLevel.save()
    newStep=(StepForUser.objects.filter(mail=mail)
                                .filter(levelNumber=levelNumber)
                                .filter(stepNumber=stepNumber)).first()
    newStep.isCurrStep=True
    newStep.save()

    oldStep=(StepForUser.objects.filter(mail=mail)
                                .filter(isCurrStep=True)).first()
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
        try:
            backLevel=int(request.data.get('backLevel'))
        except Level.DoesNotExist:
            return Response('')
        # oldLevel=Level.objects.get(levelNumber=backLevel)
        # oldLevel.isDone=False
        # oldLevel.save()
    oldStep=(StepForUser.objects.filter(mail=mail)
                                .filter(isCurrStep=True)).first()
    oldStep.isCurrStep=False
    oldStep.save()
    
    newStep=(StepForUser.objects.filter(mail=mail)
                                .filter(levelNumber=levelNumber)
                                .filter(stepNumber=stepNumber)).first()
    newStep.isCurrStep=True
    newStep.isDone=False
    newStep.save()

    
    timeLine=path(mail)
    return Response(timeLine)

#------------------------------- help functions ----------------------------------#
def path(mail):
    currlevel=(StepForUser.objects.filter(mail=mail)
                                .filter(isCurrStep=True)
                                .first()).levelNumber
    
    allStep=StepForUser.objects.filter(mail=mail)
    allLevel=Level.objects.all()
    timeLine=[]
    for level in allLevel:
        levelsir=LevelSerializer(level).data
        if level.levelNumber <= currlevel:
            levelsir['isDone']=True
        else:
            levelsir['isDone']=False
        tempLevel=[levelsir,]
        stepOfLevel=allStep.filter(levelNumber=level.levelNumber)
        stepsOfLevelSir=StepForUserSerializer(stepOfLevel,many=True)
        tempLevel+=stepsOfLevelSir.data
        timeLine.append(tempLevel)
        
    return timeLine   

