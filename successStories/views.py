from django.shortcuts import render

# Create your views here.

from .models import SuccessStories
from user.models import User
from user.serializers import UserSerializer
from .serializers import SuccessStoriesSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def allSuccessStories(request):
    successStories = SuccessStories.objects.all()
    listStories=[]
    for successStory in successStories:
        user=User.objects.get(mail=successStory.mail)
        userSerializer=UserSerializer(user).data
        del userSerializer["password"]
        tempSuccessStory=SuccessStoriesSerializer(successStory).data
        del tempSuccessStory["mail"]
        tempSuccessStory['user']=userSerializer
        listStories.append(tempSuccessStory) 
    return Response(listStories)


@api_view(['POST'])
def addSuccessStory(request):
    serializer = SuccessStoriesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def updateSuccessStory(request):
    SuccessStory = SuccessStories.objects.get(id=(request.data.get('id')))
    serializer = SuccessStoriesSerializer(SuccessStory, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def deleteSuccessStory(request):
    try:
        SuccessStory = SuccessStories.objects.get(id=(request.data.get('id')))
    except SuccessStories.DoesNotExist:
        return Response({'message': 'ERROR'})
    SuccessStory.delete()
    return Response({'message': 'deleted successfuly'})
