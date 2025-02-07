from django.contrib.auth.models import User
from django.db import models

class DailyGoal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    goal = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)
    date = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.goal} on {self.date}"

    def mark_as_completed(self):
        self.is_completed = True
        self.save()
