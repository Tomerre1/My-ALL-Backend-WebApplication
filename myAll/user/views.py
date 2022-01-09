from step.serializers import StepForUserSerializer
from .models import User
from step.models import Step , StepForUser
from .serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
#token=5cbce175d45037d379e125dd7a65104063e8b7a5

@api_view(['POST'])
def userAuthentication(request):
    mail=request.data.get('mail')
    password=request.data.get('password')
    try:
        user = User.objects.get(mail=mail)
    except User.DoesNotExist:
        return Response(None)
    if user.password == password:
        serializer= UserSerializer(user)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(None)

@api_view(['POST'])
def signUp(request):
    serializer=UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        stepForUser(serializer.data)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)




@api_view(['PUT'])
def updateUser(request):
    if request.method == 'PUT':
        user=User.objects.get(mail=request.data.get('mail'))
        serializer=UserSerializer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def getAllUsers(request):
    users=User.objects.all()
    serializer= UserSerializer(users ,many=True)
    return Response(serializer.data)


def stepForUser(user):
    for step in Step.objects.all():
        sfu=StepForUser(mail=user['mail'],
                        levelNumber=step.levelNumber,
                        stepNumber=step.stepNumber,
                        description=step.description,
                        date=step.date,
                        requirements=step.requirements)
        sfu.save()
        
    