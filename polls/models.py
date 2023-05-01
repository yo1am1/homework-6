from django.db import models


# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=24)
    subjects = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=200)
    capacity = models.IntegerField(default=1)

    def __str__(self):
        return self.name
