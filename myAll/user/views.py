
from .models import User
from medicine.views import medicineForUser
from step.views import stepForUser
from .serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def userAuthentication(request):
    mail = request.data.get('mail')
    password = request.data.get('password')
    try:
        user = User.objects.get(mail=mail)
    except User.DoesNotExist:
        return Response('')
    if user.password == password:
        serializer= UserSerializer(user)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response('')


@api_view(['POST'])
def signUp(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        stepForUser(serializer.data)
        medicineForUser(serializer.data['mail'],1)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def updateUser(request):
    if request.method == 'PUT':
        try:
            user = User.objects.get(mail=request.data.get('mail'))
        except User.DoesNotExist:
            return Response('')
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    
@api_view(['GET'])
def getAllUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)
    
@api_view(['DELETE'])
def deleteUser(request):
    try:
        user = User.objects.get(mail=request.data.get('mail'))
    except User.DoesNotExist:
        return Response({'message': 'ERROR'})
    user.delete()
    return Response({'message': 'deleted successfuly'})


#-------------------help functions ------------------#


  


        
    
