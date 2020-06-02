from django.db import models


class div(models.Model):
    title = models.CharField(max_length=40)

    def __str__(self):
        return self.title
    
class student(models.Model):
    fullname = models.CharField(max_length=30)
    rollnumber = models.IntegerField()
    mobile = models.IntegerField()
    div = models.ForeignKey(to=div,on_delete=models.CASCADE)


