
from .models import Workshop
from .serializers import WorkshopSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def allWorkshops(request):
    workshops = Workshop.objects.filter(mail=request.data.get('mail'))
    serializer = WorkshopSerializer(workshops, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addWorkshop(request):
    serializer = WorkshopSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def updateWorkshop(request):
    workshop = Workshop.objects.get(id=(request.data.get('id')))
    serializer = WorkshopSerializer(workshop, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def deleteWorkshop(request):
    try:
        workshop = Workshop.objects.get(id=(request.data.get('id')))
    except Workshop.DoesNotExist:
        return Response({'message': 'ERROR'})
    workshop.delete()
    return Response({'message': 'deleted successfuly'})

@api_view(['POST'])
def changeActive(request):
    id=request.data.get('id')
    workshop= Workshop.objects.get(id=id)
    workshop.isDone=not(workshop.isDone)
    workshop.save()
    return Response(WorkshopSerializer(workshop).data)