from django.contrib.auth.models import User
from django.db import models
from .therapist import Therapist

class TherapistPatient(models.Model):
    therapist = models.ForeignKey(Therapist, on_delete=models.CASCADE)
    patient = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.therapist.name} - {self.patient.username}"