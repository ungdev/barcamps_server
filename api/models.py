from django.db import models
import os

# Create your models here.
class Barcamp(models.Model):
    # fields
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    date = models.DateTimeField(unique=True)

class Speaker(models.Model):
    # fields
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

class Talk(models.Model):
    # relations
    barcamp_id = models.ForeignKey(Barcamp, related_name="talks_ids", on_delete=models.CASCADE)
    speaker_id = models.ForeignKey(Speaker, related_name="talks_ids", on_delete=models.CASCADE)
    # fields
    title = models.CharField(max_length=200)
    description = models.TextField()
    slides = models.FileField(null=True, upload_to='slides')
