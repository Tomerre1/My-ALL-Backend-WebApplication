import json
from django.test import TestCase
from django.test import Client
from successStories.models import SuccessStories
from user.models import User

class userTestCreate(TestCase):
    def setUp(self):
        self.user = User.objects.get_or_create(
            mail='testMail@gmail.com',
            fullname='test_fullname',
            password='1234567',
            userType='מטופל',
        
    )
        
    def test_check_user_is_created(self):
        user = User.objects.get(mail=self.user[0].mail)
        self.assertNotEqual(user.mail,None)
      
    def test_login(self):
        c = Client()
        response = c.post('/login/',{"mail":"testMail@gmail.com","password":"1234567"})
        response.status_code
        self.assertNotEqual(response.status_code, 404) 

    def test_signup(self):
        c = Client()
        response = c.post('/signup/', {'mail':"testMail@gmail.com",'fullname':"testFullName",'password':"testPassword",'userType':"testUserType"})
        response.status_code
        self.assertNotEqual(response.status_code, 404)

    
    def test_getalluser(self):
        c = Client()
        response = c.get('/getalluser/')
        response.status_code
        self.assertEqual(response.status_code, 200)

    def test_deleteUser(self):
        c = Client()
        response = c.delete('/deleteuser/', mail="testMail@gmail.com")
        response.status_code
        self.assertEqual(response.status_code, 200)

   
    
    