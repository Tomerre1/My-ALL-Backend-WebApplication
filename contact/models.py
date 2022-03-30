from django.db import models

class Contact(models.Model):
    
    id =models.TextField(max_length=100,primary_key=True)
    mailUser = models.EmailField(max_length=100)
    name =models.CharField(max_length=100)
    phone =models.CharField(max_length=15)
    mail = models.EmailField(max_length=100)
    job =models.CharField(max_length=100)
    img=models.URLField( max_length=1500)

    def __str__(self):
        return 'Name:{0} ,job: {1},phone: {2}'.format(self.name, self.job, self.phone)
