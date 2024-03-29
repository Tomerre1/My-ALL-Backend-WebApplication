from django.db import models

class SuccessStories(models.Model):
    
    id = models.TextField(max_length=100,primary_key=True)
    mail = models.EmailField(max_length=100)
    title =models.CharField(max_length=100)
    content = models.CharField(max_length=1500)
    date =models.CharField(max_length=100)
    

    def __str__(self):
        return 'id:{0} ,title: {1},content: {2}'.format(self.id, self.title, self.content)
