from django.contrib import admin
from .models import UserProfile, MoodEntry, Therapist

admin.site.register(UserProfile)
admin.site.register(MoodEntry)
admin.site.register(Therapist)
