from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Mensajes (models.Model):
    autor = models.CharField (max_length=40)
    mensaje =  models.CharField (max_length=400)
    destinatario = models.CharField (max_length=40)

class avatar (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="avatares", null=True, blank=True)