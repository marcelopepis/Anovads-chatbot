from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Log(models.Model):
  pergunta = models.CharField(max_length=200, blank=False)
  


