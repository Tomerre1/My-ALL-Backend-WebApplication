from django.db import models

class Video(models.Model):
    videoName =models.CharField(max_length=100,primary_key=True)
    videoDescription=models.CharField(max_length=1500)
    videoUrl=models.URLField( max_length=200)

    def __str__(self):
        return 'vedio Name:{0} ,description: {1}'.format(self.videoName, self.videoDescription)
