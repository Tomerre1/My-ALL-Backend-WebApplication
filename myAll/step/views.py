from re import T
from django.shortcuts import render
from level.serializers import LevelSerializer
from step.serializers import StepForUserSerializer
from level.models import Level
from user.models import User
from .models import  StepForUser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST'])
def getPath(request):
    mail=request.data.get('mail')
    timeLine=path(mail)
    return Response(timeLine)



#-------------------help functions ------------------#
def path(mail):
    allStep=StepForUser.objects.filter(mail=mail)
    allLevel=Level.objects.all()
    timeLine=[]
    for level in allLevel:

        levelsir=LevelSerializer(level)
        tempLevel=[levelsir.data,]

        stepOfLevel=allStep.filter(levelNumber=level.levelNumber)
        stepsOfLevelSir=StepForUserSerializer(stepOfLevel,many=True)
        tempLevel+=stepsOfLevelSir.data

        timeLine.append(tempLevel)
        
    return timeLine   

