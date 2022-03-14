
from .models import Tip
from user.models import User
from user.serializers import UserSerializer
from .serializers import TipSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def allTips(request):
    tips = Tip.objects.all()
    listTip=[]
    for tip in tips:
        user=User.objects.get(mail=tip.mail)
        userSerializer=UserSerializer(user).data
        del userSerializer["password"]
        tempTip=TipSerializer(tip).data
        del tempTip["mail"]
        tempTip['user']=userSerializer
        listTip.append(tempTip)
    return Response(listTip)


@api_view(['POST'])
def addTip(request):
    serializer = TipSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def updateTip(request):
    tip = Tip.objects.get(id=(request.data.get('id')))
    serializer = TipSerializer(tip, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def deleteTip(request):
    try:
        tip = Tip.objects.get(id=(request.data.get('id')))
    except Tip.DoesNotExist:
        return Response({'message': 'ERROR'})
    tip.delete()
    return Response({'message': 'deleted successfuly'})
