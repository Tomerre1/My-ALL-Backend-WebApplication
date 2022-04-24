import json
from django.test import TestCase
from django.test import Client
from tip import views
from tip.models import Tip
from user.models import User

class tipTestCreate(TestCase):
    def setUp(self):
        self.user = User.objects.get_or_create(
            mail='testMail@gmail.com',
            fullname='test_fullname',
            password='1234567',
            userType='מטופל',
        
    )
        self.tip = Tip.objects.get_or_create(
           
            id = "123",
            mail = 'testMail@gmail.com',
            title ="test_title",
            content = "test_content",
            date ="20/4/2015",
            
            )
    def test_check_user_is_created(self):
        user = User.objects.get(mail=self.user[0].mail)
        self.assertNotEqual(user.mail,None)
            
    def test_check_tip_is_created(self):
        tip = Tip.objects.get(id=self.tip[0].id)
        self.assertNotEqual(tip.id,None)   
    
    def test_get_all_tips(self):
        c = Client()
        response = c.get('/tip/alltips/')
        response.status_code
        self.assertEqual(response.status_code, 200) 

    def test_add_tip(self):
        c = Client()
        response = c.post('/tip/addtip/', {'id':"1",'mail':"testMail@gmail.com",'title':"testTitle",'content':"testContent",'date':"testDate"})
        response.status_code
        self.assertEqual(response.status_code, 200)

    
    def test_deletetip(self):
        c = Client()
        response = c.delete('/tip/deletetip/', id='123')
        response.status_code
        self.assertEqual(response.status_code, 200)
    