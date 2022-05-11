import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from contact.serializers import ContactSerializer
from level.models import Level
from level.serializers import LevelSerializer
from medicine.serializers import MedicineSerializer
from medicine.views import medicineForUser
from step.views import stepForUser
from successStories.serializers import SuccessStoriesSerializer
from tip.serializers import TipSerializer
from user.serializers import UserSerializer
from video.serializers import VideoSerializer
from medicine.models import Medicine,MedicineForUser
from step.models import Step,StepForUser
from step.serializers import StepSerializer
from user.models import User
from contact.models import Contact
from successStories.models import SuccessStories
from tip.models import Tip
from visit.models import Visit
from video.models import Video
from visit.serializers import VisitSerializer
from workshop.models import Workshop
from workshop.serializers import WorkshopSerializer


@api_view(['POST'])
def createNewDB(request):
    deleteAll()
    f = open(r'data.json', encoding="utf8")
    data = json.load(f)
    for i in data['levels']:
        serializer = LevelSerializer(data=i)
        if serializer.is_valid():
            serializer.save()
    for i in data['videos']:
        serializer = VideoSerializer(data=i)
        if serializer.is_valid():
            serializer.save()
    for i in data['steps']:
        serializer = StepSerializer(data=i)
        if serializer.is_valid():
            serializer.save()
    for i in data['medicines']:
        serializer = MedicineSerializer(data=i)
        if serializer.is_valid():
            serializer.save()
    privateData(data)
    f.close()

    return Response("success creating")
        

def deleteAll():
    User.objects.all().delete()
    Level.objects.all().delete()
    Step.objects.all().delete()
    StepForUser.objects.all().delete()
    Medicine.objects.all().delete()
    MedicineForUser.objects.all().delete()
    Contact.objects.all().delete()
    Tip.objects.all().delete()
    SuccessStories.objects.all().delete()
    Visit.objects.all().delete()
    Video.objects.all().delete()
    Workshop.objects.all().delete()

def privateData(data):
    for i in data['users']:
         serializer = UserSerializer(data=i)
         if serializer.is_valid():
            serializer.save()
            if(serializer.data["userType"]=="מטופל"):
                stepForUser(serializer.data)
                medicineForUser(serializer.data['mail'],1)

    for i in data['tips']:
        serializer = TipSerializer(data=i)
        if serializer.is_valid():
            serializer.save()

    for i in data['successStories']:
        serializer = SuccessStoriesSerializer(data=i)
        if serializer.is_valid():
            serializer.save()

    for i in data['contacts']:
        serializer = ContactSerializer(data=i)
        if serializer.is_valid():
            serializer.save()

    for i in data['visits']:
        serializer = VisitSerializer(data=i)
        if serializer.is_valid():
            serializer.save()

    for i in data['workshops']:
        serializer = WorkshopSerializer(data=i)
        if serializer.is_valid():
            serializer.save()
    

