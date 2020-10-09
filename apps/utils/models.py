from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class Timestamps(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True


