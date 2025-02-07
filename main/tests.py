from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from main.models import MoodEntry, DailyGoal, Therapist, TherapistPatient, ActivityLog

class ModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.therapist = Therapist.objects.create(name='Dr. Smith', specialization='Psychology', contact_email='dr.smith@example.com', phone_number='1234567890')

    def test_mood_entry_creation(self):
        mood_entry = MoodEntry.objects.create(user=self.user, mood='Happy', notes='Feeling great!')
        self.assertEqual(mood_entry.user.username, 'testuser')
        self.assertEqual(mood_entry.mood, 'Happy')

    def test_daily_goal_creation(self):
        daily_goal = DailyGoal.objects.create(user=self.user, goal='Exercise', date='2023-10-10')
        self.assertEqual(daily_goal.user.username, 'testuser')
        self.assertEqual(daily_goal.goal, 'Exercise')

    def test_therapist_creation(self):
        self.assertEqual(self.therapist.name, 'Dr. Smith')
        self.assertEqual(self.therapist.specialization, 'Psychology')

    def test_therapist_patient_creation(self):
        therapist_patient = TherapistPatient.objects.create(therapist=self.therapist, patient=self.user)
        self.assertEqual(therapist_patient.therapist.name, 'Dr. Smith')
        self.assertEqual(therapist_patient.patient.username, 'testuser')

    def test_activity_log_creation(self):
        activity_log = ActivityLog.objects.create(user=self.user, activity='Running', duration_minutes=30)
        self.assertEqual(activity_log.user.username, 'testuser')
        self.assertEqual(activity_log.activity, 'Running')

class ViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

    def test_dashboard_view(self):
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/dashboard.html')

    def test_register_view(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/register.html')

    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_logout_view(self):
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/logout_confirmation.html')

    def test_mood_entries_view(self):
        response = self.client.get(reverse('mood-entries'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/mood_entries.html')

    def test_view_goals_view(self):
        response = self.client.get(reverse('view-goals'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/view_goals.html')

class URLTests(TestCase):
    def test_urls(self):
        self.assertEqual(reverse('dashboard'), '/')
        self.assertEqual(reverse('register'), '/register/')
        self.assertEqual(reverse('login'), '/accounts/login/')
        self.assertEqual(reverse('logout'), '/accounts/logout/') 
        self.assertEqual(reverse('mood-entries'), '/mood-entries/')
        self.assertEqual(reverse('view-goals'), '/goals/')
