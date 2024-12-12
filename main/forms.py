from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile, DailyGoal

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    date_of_birth = forms.DateField(required=False)
    gender = forms.ChoiceField(choices=UserProfile.gender, required=False)

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
    class Meta:
        model = DailyGoal
        fields = ['goal', 'date']