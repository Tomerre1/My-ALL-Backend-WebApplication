from django.db import models
from django.db.models import JSONField


class Medicine(models.Model):
    medicineName=models.CharField(max_length=100,primary_key=True)
    description=models.CharField(max_length=1500)
    level=JSONField(default=list, blank=True, null=True)
    count=models.CharField(max_length=100,null=True,default=None)
    badInfluence=models.CharField(max_length=1000,null=True,default=None)
    foodOrNot=models.CharField(max_length=100,null=True,default=None)


    def __str__(self):
        return 'medicine Name:{0} ,description: {1}, level: {2}'.format(self.medicineName, self.description, self.level) 
