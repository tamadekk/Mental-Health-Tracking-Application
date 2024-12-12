import random
from .models import DailyGoal, MoodEntry, ActivityLog, Therapist, UserProfile
from django.contrib.auth.models import User
import factory
from factory.django import DjangoModelFactory

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('user_name')
    email = factory.Faker('email')
    password = 'password123'

class UserProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserProfile

    user = factory.SubFactory(UserFactory)
    date_of_birth = factory.Faker('date_of_birth')
    gender = random.choice(['Male', 'Female', 'Other'])

class DailyGoalFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = DailyGoal

    user = factory.SubFactory(UserFactory)
    goal = factory.Faker('sentence', nb_words=6)
    is_completed = factory.LazyFunction(lambda: random.choice([True, False]))
    date = factory.Faker('date_this_year')

class MoodEntryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = MoodEntry

    user = factory.SubFactory(UserFactory)
    mood = random.choice(['Happy', 'Sad', 'Angry', 'Stressed', 'Neutral'])
    notes = factory.Faker('text')
    created_at = factory.Faker('date_this_year')

class ActivityLogFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ActivityLog

    user = factory.SubFactory(UserFactory)
    activity = factory.Faker('word')
    duration_minutes = factory.LazyFunction(lambda: random.randint(15, 120))
    notes = factory.Faker('text')
    logged_at = factory.Faker('date_this_year')

class TherapistFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Therapist

    name = factory.Faker('name')
    specialization = factory.Faker('word')
    contact_email = factory.Faker('email')
    phone_number = factory.Faker('phone_number')
