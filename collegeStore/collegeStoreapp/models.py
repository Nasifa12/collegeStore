from django.db import models


# Create your models here.
class Student(models.Model):
    Name = models.CharField(max_length=250)
    DOB = models.DateField()
    Age = models.IntegerField()
    PhoneNumber = models.IntegerField()
    MailID = models.EmailField(max_length=250)
    Address = models.TextField(max_length=250)
    Department = models.TextField(max_length=250)
    Courses = models.CharField(max_length=250)
    Purpose = models.CharField(max_length=250)
    Materials = models.CharField(max_length=250)

    def __str__(self):
        return self.name
