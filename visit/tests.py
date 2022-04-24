import json
from django.test import TestCase
from django.test import Client
from visit import views
from visit.models import Visit
from visit.serializers import VisitSerializer
from user.models import User

class visitTestCreate(TestCase):
    def setUp(self):
        self.user = User.objects.get_or_create(
            mail='testMail@gmail.com',
            fullname='test_fullname',
            password='1234567',
            userType='מטופל',
        
    )
        self.visit = Visit.objects.get_or_create(
            id='123',
            mail = "testMail@gmail.com",
            content ="test_content",
            title ="test_title",
            date = "20/4/2015",
            )
    def test_check_user_is_created(self):
        user = User.objects.get(mail=self.user[0].mail)
        self.assertNotEqual(user.mail,None)
            
    def test_check_visit_is_created(self):
        visit = Visit.objects.get(id=self.visit[0].id)
        self.assertNotEqual(visit.id,None)   
    
    def test_get_all_visits(self):
        c = Client()
        response = c.post('/visit/allvisits/', {'mail':"testMail@gmail.com"})
        response.status_code
        self.assertEqual(response.status_code, 200) 

    def test_add_visit(self):
        c = Client()
        response = c.post('/visit/addvisit/', {'id':"1234",'mail':"testMail@gmail.com",'title':"testTitle",'content':"testContent",'date':"testDate"})
        response.status_code
        self.assertEqual(response.status_code, 200)

    
    def test_deletevisit(self):
        c = Client()
        response = c.delete('/visit/deletevisit/', id='123')
        response.status_code
        self.assertEqual(response.status_code, 200)

    def test_changeactive(self):
        c = Client()
        response = c.post('/visit/changeactive/', {"id":'123'})
        response.status_code
        self.assertEqual(response.status_code, 200)