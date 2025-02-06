from django.contrib import admin

from .models import UserProfile, MoodEntry, Therapist, DailyGoal, TherapistPatient

admin.site.register(UserProfile)
admin.site.register(MoodEntry)
admin.site.register(Therapist)
admin.site.register(DailyGoal)
admin.site.register(TherapistPatient)

