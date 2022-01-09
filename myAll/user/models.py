from django.db import models

# Create your models here.
class User(models.Model):
    mail=models.EmailField(max_length=254,primary_key=True)
    fullname = models.CharField(max_length=50)
    password = models.CharField(max_length=40)
    userType=models.CharField(max_length=40,null=True,default=None)
    

    def __str__(self):
        return 'full name:{0} ,mail: {1},type user:{2}'.format(self.fullname, self.mail,self.userType) 
    