from django.db import models

class Step(models.Model):
    levelNumber=models.IntegerField()
    stepNumber=models.IntegerField()
    description=models.CharField(max_length=1500)
    date=models.DateTimeField(null=True,default=None)
    requirements=models.CharField(max_length=1500,null=True,default=None)
    class Meta:
        unique_together = (('levelNumber', 'stepNumber'),)

    def __str__(self):
        return 'levelNumber:{0} ,stepNumber:{2},description: {1}'.format(self.levelNumber, self.description,self.stepNumber)




class StepForUser(models.Model):
    mail=models.EmailField(max_length=254)
    levelNumber=models.IntegerField()
    stepNumber=models.IntegerField()
    description=models.CharField(max_length=1500)
    date=models.DateTimeField(null=True,default=None)
    requirements=models.CharField(max_length=1500,null=True,default=None)
    isDone=models.BooleanField(default=False)
    isCurrStep=models.BooleanField(default=False)

    class Meta:
        unique_together = (('mail','levelNumber', 'stepNumber'),)

    def __str__(self):
        return 'user mail:{0},levelNumber:{1} ,stepNumber:{3},description: {2}'.format(self.mail,self.levelNumber, self.description,self.stepNumber) 
