from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import UserProfile, DailyGoal, MoodEntry, Therapist, TherapistPatient

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    date_of_birth = forms.DateField(required=False)
    gender = forms.ChoiceField(choices=UserProfile.gender, required=False)
    password1 = forms.CharField(
        widget=forms.PasswordInput(),
        help_text=None
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(),
        help_text=None 
    )
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'date_of_birth', 'gender']

    def save(self, commit=True):
        user = super().save(commit=False)
        user_profile = UserProfile(user=user, date_of_birth=self.cleaned_data['date_of_birth'], gender=self.cleaned_data['gender'])
        if commit:
            user.save()
            user_profile.save()
        return user


class DailyGoalForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    is_completed = forms.BooleanField(required=False, label='Mark as completed')

    class Meta:
        model = DailyGoal
        fields = ['goal', 'date', 'is_completed']

class MoodEntryForm(forms.ModelForm):
    class Meta:
        model = MoodEntry
        fields = ['mood', 'notes']

class TherapistForm(forms.ModelForm):
    class Meta:
        model = Therapist
        fields = ['name', 'specialization', 'phone_number', 'contact_email']

class AssignPatientForm(forms.ModelForm):
    class Meta:
        model = TherapistPatient
        fields = ['therapist', 'patient']