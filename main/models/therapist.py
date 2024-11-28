from django.contrib.auth.models import User
from django.db import models


class Therapist(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    contact_email = models.EmailField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name
