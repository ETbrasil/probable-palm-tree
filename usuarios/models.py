from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    foto_user = models.ImageField(null=True, blank=True, upload_to='fotos/%d/%m/%Y/')
    user = models.OneToOneField ( 
        User, 
        on_delete = models.CASCADE
    )