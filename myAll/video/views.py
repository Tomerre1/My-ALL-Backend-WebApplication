
from .models import Video
from .serializers import VideoSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def allVideos(request):
    videos = Video.objects.all()
    serializer = VideoSerializer(videos, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addVideo(request):
    serializer = VideoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def updateVideo(request):
    video = Video.objects.get(videoName=(request.data.get('videoName')))
    serializer = VideoSerializer(video, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def deleteVideo(request):
    try:
        video = Video.objects.get(videoName=(request.data.get('videoName')))
    except Video.DoesNotExist:
        return Response({'message': 'ERROR'})
    video.delete()
    return Response({'message': 'deleted successfuly'})
