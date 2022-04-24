import json
from django.test import TestCase
from django.test import Client
from contact import views
from contact.models import Contact
from contact.serializers import ContactSerializer
from user.models import User

class contactTestCreate(TestCase):
    def setUp(self):
        self.user = User.objects.get_or_create(
            mail='testMail@gmail.com',
            fullname='test_fullname',
            password='1234567',
            userType='מטופל',
        
    )
        self.contant = Contact.objects.get_or_create(
            id='123',
            mailUser='testMail@gmail.com',
            name='test_name',
            phone='0541234567',
            mail='mail_test_contact@gmail.com',
            job="test_job",
            img="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOEAAADhCAMAAAAJbSJIAAAAe1BMVEX///8dHRsAAAAZGRcuLi3Ly8sbGxnOzs4VFROpqakQEA21tbVpaWjBwcHx8fHp6elgYGAHBwA5OTednZzV1dXm5ubU1NTb29smJiRdXVy6urlWVlWYmJeKiorz8/Ourq5MTEt5eXlvb26Ojo2bm5oxMS+Dg4NERENJSUiSrgQ+AAADIElEQVR4nO3ZZ3uiQBSGYRwQEUtCMGIsiylL8v9/4RICIypTMEXIPve3cHH28C6TKcRxAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA8J9L1uM4Hs/uf6bbeuAphHNVTaqs8Vxzw1shPS709z6tlI0KK++Psd9MuCpCmXCsKTL0G0ciHFT8ULxpX+Q0UjZ6F0bKR5SGYqCkS6gu0rab3wn/+P5AxLqEYXOXsvaTAb8hYSKChorHCxO64sYYcKkL+PUJb4TbWPJ8UUJXmGeqxemQ+eaEXsMbLGqWFyT0LQIm+oBfnrBWFebzaCRfqOu1T+iLxBhwIWqqwqh+0ZxQnFM3DH3ZZBpPJs8r2VXMFCUPTc8YFD+ZAzrDg1H1yNHzqHZZWVrdLtb12w1F8pde7Mork+pKeKuoWdQfsrw72Czzn9ruFpbyka1ulwnNk1lD0fYQQIa2+QfKm8Npi6ZS9f8jJu0etk3CXVQW1bYhmQgLFrNGDxJmVcLaQB5tbgubX5HwRVSzoF2TM51PKPdPvgh3yhVQ4yoJ18fz6Ej/hHL59fNFaZq2nQ6vkfB0PVxpq+KjfUK+6A8y9drS4CoJj7l3+rLXkx2Km7/Knf1A70FC5+9ZXT5en8yH2A99SOhMG04XoeU2ox8JnaHXcETUHoIP+pHQcWYbIU5PDMqd95Huz6WVefr+Lar+Kv3u7kvT2THrhss4PxhF7cbpVRKavwTpmmZyuAavFvd3fdc2r4byS+3iU5vjU9cTVpu24Gg62gf2o6HzCT23YeJsM947n7A6H/r1qsew46N0PTql3kvLTxbu4QxcnajcgUXXLqyH+m9tr9US6Iu3NJnP72dyookyi64d2NMYhlvtC/vHB8HD3sbm22APEjqZqix8sOnag4TOPmqscYXVAaoPCZ19U2FgNUZ7ktDZnR+exMryg80nE/oF64S+imlhS/Yiqv1BKJ9ytoYKqWx6acKgYJ0wUDEv3UnmH9aWTWr/kGXT6KKEP+xmmMbbbby2+/0DAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAD/wD54Mp1IWvHPUAAAAASUVORK5CYII="
            )
    def test_check_user_is_created(self):
        user = User.objects.get(mail=self.user[0].mail)
        self.assertNotEqual(user.mail,None)
            
    def test_check_contact_is_created(self):
        contant = Contact.objects.get(id=self.contant[0].id)
        self.assertNotEqual(contant.id,None)   
    
    def test_get_all_contants(self):
        c = Client()
        response = c.post('/contact/allcontacts/', {'mailUser':"testMail@gmail.com"})
        response.status_code
        self.assertEqual(response.status_code, 200) 

    def test_add_contact(self):
        c = Client()
        response = c.post('/contact/addcontact/', {'id':"1234",'mailUser':self.contant[0].mailUser,'name':"tast",'phone':"0546814122",'mail':self.contant[0].mailUser,'job':"dr",'img':"https://www.youtube.com/"})
        response.status_code
        self.assertEqual(response.status_code, 200)

    
    def test_deletecontact(self):
        c = Client()
        response = c.delete('/contact/deletecontact/', id='123')
        response.status_code
        self.assertEqual(response.status_code, 200)
    