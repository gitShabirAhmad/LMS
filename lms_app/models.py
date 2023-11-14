from django.db import models
from account.models import Account


# Create your models here.
class Cls(models.Model):
    name = models.CharField(max_length=45)
    time = models.CharField(max_length=45)
    started_date = models.DateField(default='2023-11-6')
    students = models.ManyToManyField(Account)


    def __str__(self):
        return self.name
