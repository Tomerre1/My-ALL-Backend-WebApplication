from django.db import models

class Level(models.Model):
    levelNumber=models.IntegerField(primary_key=True)
    description=models.CharField(max_length=1500)

    def __str__(self):
        return 'levelNumber:{0} ,description: {1}'.format(self.levelNumber, self.description) 
