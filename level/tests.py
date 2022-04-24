import json
from django.test import TestCase
from django.test import Client
from level import views
from level.models import Level
from level.serializers import LevelSerializer
from user.models import User

class levelTestCreate(TestCase):
    def setUp(self):
        self.user = User.objects.get_or_create(
            mail='testMail@gmail.com',
            fullname='test_fullname',
            password='1234567',
            userType='מטופל',
        
    )
        self.level = Level.objects.get_or_create(
            levelNumber=1,
            description="test_description",
            )
    def test_check_user_is_created(self):
        user = User.objects.get(mail=self.user[0].mail)
        self.assertNotEqual(user.mail,None)
            
    def test_check_level_is_created(self):
        level = Level.objects.get(levelNumber=self.level[0].levelNumber)
        self.assertNotEqual(level.levelNumber,None)   
    
    def test_get_all_levels(self):
        c = Client()
        response = c.get('/level/getAllLevels/')
        response.status_code
        self.assertEqual(response.status_code, 200) 

    def test_add_level(self):
        c = Client()
        response = c.post('/level/InsertLevel/', {'levelNumber':6,"description":"description test"})
        response.status_code
        self.assertEqual(response.status_code, 201)

    
    def test_deletelevel(self):
        c = Client()
        response = c.delete('/level/deleteLevel/', levelNumber=1)
        response.status_code
        self.assertEqual(response.status_code, 200)
        
    