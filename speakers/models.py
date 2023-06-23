from django.db import models

class Speaker(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField()
    contact_info = models.CharField(max_length=255)
    profile_picture = models.ImageField(upload_to='speakers/')
    expertise = models.CharField(max_length=255)
