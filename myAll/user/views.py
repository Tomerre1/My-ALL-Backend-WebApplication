from .models import User
from .serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
#token=5cbce175d45037d379e125dd7a65104063e8b7a5

@api_view(['POST'])
def userAuthentication(request):
    
    userId=int(request.data.get('userId'))
    password=request.data.get('password')
    try:
        user = User.objects.get(userId=userId)
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
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['PUT'])
def updateUser(request):
    if request.method == 'PUT':
        user=User.objects.get(userId=int(request.data.get('userId')))
        serializer=UserSerializer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def getAllUsers(request):
    users=User.objects.all()
    serializer= UserSerializer(users ,many=True)
    print(serializer.data)
    return Response(serializer.data)
    