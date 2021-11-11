from django.db import models

# Create your models here.
class User(models.Model):
    userId=models.IntegerField(primary_key=True)
    fullname = models.CharField(max_length=50)
    password = models.CharField(max_length=40)
    userType=models.CharField(max_length=40,null=True,default=None)
    parentId = models.IntegerField(default=None,null=True)

    def __str__(self):
        return 'full name:{0} ,user Id: {1}, parent id: {2},type user:{3}'.format(self.fullname, self.userId,self.parentId,self.userType) 
    