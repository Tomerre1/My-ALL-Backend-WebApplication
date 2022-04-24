import json
from django.test import TestCase
from django.test import Client
from workshop import views
from workshop.models import Workshop
from workshop.serializers import WorkshopSerializer
from user.models import User

class workshopTestCreate(TestCase):
    def setUp(self):
        self.user = User.objects.get_or_create(
            mail='testMail@gmail.com',
            fullname='test_fullname',
            password='1234567',
            userType='מטופל',
        
    )
        self.workshop = Workshop.objects.get_or_create(
            id='123',
            mail = "testMail@gmail.com",
            content ="test_content",
            title ="test_title",
            lecturer="dr test",
            date = "20/4/2015",
            )
    def test_check_user_is_created(self):
        user = User.objects.get(mail=self.user[0].mail)
        self.assertNotEqual(user.mail,None)
            
    def test_check_workshop_is_created(self):
        workshop = Workshop.objects.get(id=self.workshop[0].id)
        self.assertNotEqual(workshop.id,None)   
    
    def test_get_all_workshops(self):
        c = Client()
        response = c.post('/workshop/allworkshops/', {'mail':"testMail@gmail.com"})
        response.status_code
        self.assertEqual(response.status_code, 200) 

    def test_add_workshop(self):
        c = Client()
        response = c.post('/workshop/addworkshop/', {'id':"1234","lecturer":"dr test",'mail':"testMail@gmail.com",'title':"testTitle",'content':"testContent",'date':"testDate"})
        response.status_code
        self.assertEqual(response.status_code, 200)

    
    def test_deleteworkshop(self):
        c = Client()
        response = c.delete('/workshop/deleteworkshop/', id='123')
        response.status_code
        self.assertEqual(response.status_code, 200)
        
    def test_changeactive(self):
        c = Client()
        response = c.post('/workshop/changeactive/', {"id":'123'})
        response.status_code
        self.assertEqual(response.status_code, 200)