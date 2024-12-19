from django.contrib import admin
from .models import UserProfile, MoodEntry, Therapist, DailyGoal

admin.site.register(UserProfile)
admin.site.register(MoodEntry)
admin.site.register(Therapist)
admin.site.register(DailyGoal)

