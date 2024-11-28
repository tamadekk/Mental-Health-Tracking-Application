from django.contrib.auth.models import User
from django.db import models


class MoodEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mood = models.CharField(max_length=20, choices=[
        ('Happy', 'Happy'),
        ('Sad', 'Sad'),
        ('Angry', 'Angry'),
        ('Stressed', 'Stressed'),
        ('Neutral', 'Neutral'),
    ])
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.mood} on {self.created_at.date()}"
