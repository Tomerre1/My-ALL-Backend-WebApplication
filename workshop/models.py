from django.db import models


class Workshop(models.Model):
    id =models.IntegerField(primary_key=True)
    mail = models.EmailField(max_length=100)
    content =models.CharField(max_length=1500)
    title =models.CharField(max_length=100)
    lecturer=models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    isDone = models.BooleanField(default=False)

    def __str__(self):
        return 'id:{0} ,mail: {1},title: {2},lecturer: {3}'.format(self.id, self.mail, self.title, self.lecturer)
