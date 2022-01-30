from django.db import models
from django.db.models import JSONField


class Medicine(models.Model):
    medicineName=models.CharField(max_length=100,primary_key=True)
    description=models.CharField(max_length=1500)
    levels=JSONField(default=list, blank=True, null=True)
    count=models.CharField(max_length=100,null=True,default=None)
    badInfluence=JSONField(default=list, blank=True, null=True)
    foodOrNot=models.CharField(max_length=100,null=True,default=None)
    days=JSONField(default=list, blank=True, null=True)

    def __str__(self):
        return 'medicine Name:{0} ,description: {1}, level: {2}'.format(self.medicineName, self.description, self.levels) 


class MedicineForUser(models.Model):
    mail=models.EmailField(max_length=254)
    medicineName=models.CharField(max_length=100)
    count=models.CharField(max_length=100,null=True,default=None)
    days=JSONField(default=dict, blank=True, null=True)
    class Meta:
        unique_together = (('mail','medicineName'),)


    def __str__(self):
        return 'mail:{1},medicine Name:{0} '.format(self.medicineName, self.mail) 

