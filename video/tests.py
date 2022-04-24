import json
from django.test import TestCase
from django.test import Client
from video import views
from video.models import Video
from video.serializers import VideoSerializer
from user.models import User

class videoTestCreate(TestCase):
    def setUp(self):
        self.user = User.objects.get_or_create(
            mail='testMail@gmail.com',
            fullname='test_fullname',
            password='1234567',
            userType='מטופל',
        
    )
        self.video = Video.objects.get_or_create(
            videoName ="test_name",
            videoDescription="test_videoDescription",
            videoUrl="https://www.youtube.com/watch?v=ckObp0fTNmU",
            )
    def test_check_user_is_created(self):
        user = User.objects.get(mail=self.user[0].mail)
        self.assertNotEqual(user.mail,None)
            
    def test_check_video_is_created(self):
        video = Video.objects.get(videoName=self.video[0].videoName)
        self.assertNotEqual(video.videoName,None)   
    
    def test_get_all_videos(self):
        c = Client()
        response = c.get('/video/allvideos/')
        response.status_code
        self.assertEqual(response.status_code, 200) 

    def test_add_video(self):
        c = Client()
        response = c.post('/video/addvideo/', {'videoName':"test_new_name",'videoDescription':"test description",'videoUrl':"https://www.youtube.com/watch?v=RsubEIFu00U"})
        response.status_code
        self.assertEqual(response.status_code, 200)

    
    def test_deletevideo(self):
        c = Client()
        response = c.delete('/video/deletevideo/', videoName="test_name")
        response.status_code
        self.assertEqual(response.status_code, 200)
    