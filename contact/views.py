
from .models import Contact
from .serializers import ContactSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST'])
def allContacts(request):
    contacts = Contact.objects.filter(mailUser=request.data.get('mailUser'))
    serializer = ContactSerializer(contacts, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addContact(request):
    serializer = ContactSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def updateContact(request):
    contact = Contact.objects.get(id=(request.data.get('id')))
    serializer = ContactSerializer(contact, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def deleteContact(request):
    try:
        contact = Contact.objects.get(id=(request.data.get('id')))
    except Contact.DoesNotExist:
        return Response({'message': 'ERROR'})
    contact.delete()
    return Response({'message': 'deleted successfuly'})
