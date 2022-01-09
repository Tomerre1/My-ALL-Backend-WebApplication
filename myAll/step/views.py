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

@api_view(['POST'])
def next(request):
    mail=request.data.get('mail')
    levelNumber=request.data.get('levelNumber')
    stepNumber=request.data.get('stepNumber')
    isNextLevel=request.data.get('isNextLevel')
    if isNextLevel:
        nextLevel=request.data.get('nextLevel')

    newStep=(StepForUser.objects.filter(mail=mail).filter(levelNumber=levelNumber).filter(stepNumber=stepNumber)).first()
    newStep.isCurrStep=True
    newStep.save()

    oldStep=StepForUser.objects.get(isCurrStep=True)
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
    isNextLevel=request.data.get('isNextLevel')
    if isNextLevel:
        nextLevel=request.data.get('nextLevel')

    newStep=(StepForUser.objects.filter(mail=mail).filter(levelNumber=levelNumber).filter(stepNumber=stepNumber)).first()
    newStep.isCurrStep=True
    newStep.isDone=False
    newStep.save()

    oldStep=StepForUser.objects.get(isCurrStep=True)
    oldStep.isCurrStep=False
    oldStep.save()
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

