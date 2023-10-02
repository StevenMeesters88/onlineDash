from django.db import models


# Create your models here.
class Document(models.Model):
    session_key = models.CharField(max_length=255)
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
