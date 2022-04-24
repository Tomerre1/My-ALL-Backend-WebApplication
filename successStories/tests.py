import json
from django.test import TestCase
from django.test import Client
from successStories.models import SuccessStories
from user.models import User

class successStoriesTestCreate(TestCase):
    def setUp(self):
        self.user = User.objects.get_or_create(
            mail='testMail@gmail.com',
            fullname='test_fullname',
            password='1234567',
            userType='מטופל',
        
    )
        self.successStory = SuccessStories.objects.get_or_create(
            id = "1",
            mail='testMail@gmail.com', 
            title ="test_title",
            content = "test_content",
            date ="22/3/20"
            )
    def test_check_user_is_created(self):
        user = User.objects.get(mail=self.user[0].mail)
        self.assertNotEqual(user.mail,None)
            
    def test_check_successStory_is_created(self):
        medicine = SuccessStories.objects.get(id="1")
        self.assertEqual(medicine.id, "1")   
    
    def test_allsuccessStories(self):
        c = Client()
        response = c.get('/successStories/allsuccessStories/')
        response.status_code
        self.assertEqual(response.status_code, 200) 

    def test_addsuccessStory(self):
        c = Client()
        response = c.post('/successStories/addsuccessStory/', {'id':"2",'mail':"testMail@gmail.com",'title':"testTitle",'content':"testContent",'date':"testDate"})
        response.status_code
        self.assertEqual(response.status_code, 200)

    
    def test_deletesuccessStory(self):
        c = Client()
        response = c.delete('/successStories/deletesuccessStory/', id="1")
        response.status_code
        self.assertEqual(response.status_code, 200)

   
    
    