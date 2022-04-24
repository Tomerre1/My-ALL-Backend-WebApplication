import json
from django.test import TestCase
from django.test import Client
from medicine.models import Medicine,MedicineForUser
from user.models import User

class medicineTestCreate(TestCase):
    def setUp(self):
        self.user = User.objects.get_or_create(
            mail='testMail@gmail.com',
            fullname='test_fullname',
            password='1234567',
            userType='מטופל',
        
    )
        self.mfu = MedicineForUser.objects.get_or_create(
            mail=self.user[0].mail,
            medicineName="test_medicineName",
            count="1 per day",
            days={"1":True},
            )
    def test_check_user_is_created(self):
        user = User.objects.get(mail=self.user[0].mail)
        self.assertNotEqual(user.mail,None)
            
    def test_check_medicine_is_created(self):
        medicine = MedicineForUser.objects.get(mail=self.user[0].mail,medicineName="test_medicineName")
        self.assertEqual(medicine.medicineName, "test_medicineName")   
    
    def test_getListMedicines(self):
        c = Client()
        response = c.post('/medicine/getListMedicines/', {'mail':"testMail@gmail.com"})
        response.status_code
        self.assertEqual(response.status_code, 200) 

    def test_addMedicineForDay(self):
        c = Client()
        response = c.post('/medicine/addMedicineForDay/', {'mail':"testMail@gmail.com","medicineName":"test_medicineName","count":"1234",'day':"שני"})
        response.status_code
        self.assertEqual(response.status_code, 200)

    
    def test_removeMedicineFromDay(self):
        c = Client()
        response = c.post('/medicine/removeMedicineFromDay/', {'mail':"testMail@gmail.com","medicineName":"test_medicineName","count":"1234",'day':"ראשון"})
        response.status_code
        self.assertEqual(response.status_code, 200)

    def test_changeActive(self):
        c = Client()
        response = c.post('/medicine/changeActive/', {'mail':"testMail@gmail.com","medicineName":"test_medicineName","count":"1234",'day':"ראשון"})
        response.status_code
        self.assertEqual(response.status_code, 200)
    
    