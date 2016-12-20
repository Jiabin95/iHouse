from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Post(models.Model):
	text = models.CharField(max_length=30)
	
class Contact(models.Model):
    """ For other types of fields for different purpose, please refer to: https://docs.djangoproject.com/ja/1.10/ref/models/fields/ """
    
    name = models.CharField(max_length=200)
    
class IMG(models.Model):
    img = models.ImageField(upload_to='upload')
