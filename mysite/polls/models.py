# models.py     
from django.contrib.auth.models import User
from django.db import models

class Person(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    
    def __str__(self):
        return self.firstname + " " + self.lastname
  
class Profile(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    city = models.CharField(max_length=100, blank=True)

