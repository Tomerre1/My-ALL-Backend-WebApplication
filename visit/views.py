
from .models import Visit
from .serializers import VisitSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST'])
def allVisits(request):
    visits = Visit.objects.filter(mail=request.data.get('mail'))
    serializer = VisitSerializer(visits, many=True)
    return Response(serializer.data)



@api_view(['POST'])
def addVisit(request):
    serializer = VisitSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def updateVisit(request):
    visit = Visit.objects.get(id=(request.data.get('id')))
    serializer = VisitSerializer(visit, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def deleteVisit(request):
    try:
        visit = Visit.objects.get(id=(request.data.get('id')))
    except Visit.DoesNotExist:
        return Response({'message': 'ERROR'})
    visit.delete()
    return Response({'message': 'deleted successfuly'})

@api_view(['POST'])
def changeActive(request):
    id=request.data.get('id')
    visit= Visit.objects.get(id=id)
    visit.isDone=not(visit.isDone)
    visit.save()
    return Response(VisitSerializer(visit).data)