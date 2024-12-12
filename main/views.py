from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

from main.forms import DailyGoalForm, MoodEntryForm
from main.models.therapist import Therapist
from .models import MoodEntry, DailyGoal


def index(request):
    return render(request, 'main/index.html')


@login_required
def dashboard(request):
    return render(request, 'main/dashboard.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created successfully! You can now log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'main/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'main/login.html')


def user_logout(request):
    logout(request)
    return render(request, 'main/logout_confirmation.html')


@user_passes_test(lambda u: u.is_superuser)
def manage_users(request):
    users = User.objects.all()
    return render(request, 'main/manage_users.html', {'users': users})


@login_required
def mood_entries(request):
    mood_entries = MoodEntry.objects.filter(user=request.user)
    return render(request, 'main/mood_entries.html', {'mood_entries': mood_entries})


@login_required
def view_goals(request):
    goals = DailyGoal.objects.filter(user=request.user)
    return render(request, 'main/view_goals.html', {'goals': goals})


@login_required
def add_mood_entry(request):
    if request.method == 'POST':
        form = MoodEntryForm(request.POST)
        if form.is_valid():
            mood_entry = form.save(commit=False)
            mood_entry.user = request.user
            mood_entry.save()
            return redirect('mood-entries')
    else:
        form = MoodEntryForm()
    return render(request, 'main/add_mood_entry.html', {'form': form})


@login_required
def daily_goals(request):
    if request.method == 'POST':
        form = DailyGoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = request.user
            goal.save()
            return redirect('daily-goals')
    else:
        form = DailyGoalForm()
    goals = DailyGoal.objects.filter(user=request.user)
    return render(request, 'main/daily_goals.html', {'daily_goals': goals, 'form': form})


@login_required
def add_daily_goal(request):
    if request.method == 'POST':
        form = DailyGoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = request.user
            goal.save()
            return redirect('daily-goals')
    else:
        form = DailyGoalForm()
    goals = DailyGoal.objects.filter(user=request.user)
    context = {
        'form': form,
        'goals': goals,
        'date_picker': True  # Pass context to enable date picker in template
    }
    return render(request, 'main/add_daily_goal.html', context)


@login_required
def therapists_list(request):
    therapists = Therapist.objects.all()
    return render(request, 'main/therapists_list.html', {'therapists': therapists})
