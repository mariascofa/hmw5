from django.db import models



class Student(models.Model):
    """This data consists of various
    fields with information about students."""

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    normalized_name = models.CharField(max_length=200, null=True)
    age = models.IntegerField(null=True)
    sex = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    birthday = models.DateField('Birthday (d/m/Y)', null=True)
    email = models.CharField(max_length=200, null=True)
    social_url = models.CharField(max_length=200, null=True)

