from django.db import models

class Profile(models.Model):
    full_name = models.CharField(max_length=200)
    bio = models.CharField(max_length=200)
    email= models.EmailField(max_length=200)
    phone = models.CharField(max_length=20)
    
    def __str__(self):
        return self.full_name
