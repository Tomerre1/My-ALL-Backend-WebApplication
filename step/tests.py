import datetime
import json
from django.test import TestCase
from django.test import Client
from level.models import Level
from step.models import Step, StepForUser
from step.serializers import StepSerializer
from user.models import User

class stepTestCreate(TestCase):
    def setUp(self):
        self.user = User.objects.get_or_create(
            mail='testMail@gmail.com',
            fullname='test_fullname',
            password='1234567',
            userType='מטופל',
        
    )
        self.step = Step.objects.get_or_create(
            levelNumber=1,
            stepNumber=2,
            description="test_description",
            #date=datetime.datetime.now(),
            requirements="test_requirements",
        )
        self.level=Level.objects.get_or_create(
            levelNumber=1,
            description="test_description"
        )

        self.sfu = StepForUser.objects.get_or_create(
            mail=self.user[0].mail,
            levelNumber=1,
            stepNumber=2,
            description="test_description",
            isCurrStep=True
        
        )
    def test_check_user_is_created(self):
        user = User.objects.get(mail=self.user[0].mail)
        self.assertNotEqual(user.mail,None)
            
    def test_check_contact_is_created(self):
        step = Step.objects.get(levelNumber=1,stepNumber=2)
        flag=self.step[0].levelNumber==step.levelNumber and self.step[0].stepNumber==step.stepNumber
        self.assertNotEqual(flag,False)   
    
    def test_get_all_steps(self):
        c = Client()
        response = c.get('/step/getAllSteps/')
        response.status_code
        self.assertEqual(response.status_code, 200) 

    def test_InsertStep(self):
        c = Client()
        response = c.post('/step/InsertStep/', {'levelNumber':1,'stepNumber':4,"description":"test_description"})
        response.status_code
        self.assertEqual(response.status_code, 201)

    def test_deletecontact(self):
        c = Client()
        response = c.delete('/step/deleteStep/',levelNumber=1,stepNumber=2)
        response.status_code
        self.assertEqual(response.status_code, 200)

    def test_getPath(self):
        c = Client()
        response = c.post('/step/timeline/',{"mail":self.sfu[0].mail})
        response.status_code
        self.assertEqual(response.status_code, 200)
        
    