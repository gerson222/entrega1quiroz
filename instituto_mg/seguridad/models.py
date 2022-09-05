from django.db import models

# Create your models here.

class Mensajes (models.Model):
    autor = models.CharField (max_length=40)
    mensaje =  models.CharField (max_length=400)
    destinatario = models.CharField (max_length=40)

    