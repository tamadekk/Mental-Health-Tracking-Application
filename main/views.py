from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.http import require_POST

from main.forms import DailyGoalForm, MoodEntryForm, TherapistForm
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
        'date_picker': True
    }
    return render(request, 'main/add_daily_goal.html', context)


@login_required
def therapists_list(request):
    therapists = Therapist.objects.all()
    return render(request, 'main/therapists_list.html', {'therapists': therapists})


class DailyGoalListView(ListView):
    model = DailyGoal
    template_name = 'main/daily_goals.html'
    context_object_name = 'goals'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = super().get_queryset().filter(user=self.request.user)
        search_query = self.request.GET.get('q', '')
        date_filter = self.request.GET.get('date', '')
        if search_query:
            queryset = queryset.filter(goal__icontains=search_query)
        if date_filter:
            queryset = queryset.filter(date=date_filter)
        return queryset

class MoodEntryListView(ListView):
    model = MoodEntry
    template_name = 'main/mood_entries.html'
    context_object_name = 'mood_entries'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = super().get_queryset().filter(user=self.request.user)
        search_query = self.request.GET.get('q', '')
        mood_filter = self.request.GET.get('mood', '')
        if search_query:
            queryset = queryset.filter(notes__icontains=search_query)
        if mood_filter:
            queryset = queryset.filter(mood=mood_filter)
        return queryset


class TherapistListView(ListView):
    model = Therapist
    template_name = 'main/therapists_list.html'
    context_object_name = 'therapists'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q', '')
        specialization_filter = self.request.GET.get('specialization', '')
        if search_query:
            queryset = queryset.filter(name__icontains=search_query)
        if specialization_filter:
            queryset = queryset.filter(specialization=specialization_filter)
        return queryset


def TherapistDetailView(request, pk):
    therapist = Therapist.objects.get(pk=pk)
    return render(request, 'main/therapist_detail.html', {
        'therapist': therapist
    })


class DailyGoalDetailView(DetailView):
    model = DailyGoal
    template_name = 'main/daily_goal_detail.html' 
    context_object_name = 'daily_goal'

class MoodEntryDetailView(DetailView):
    model = MoodEntry
    template_name = 'main/mood_entry_detail.html' 
    context_object_name = 'mood_entry'


@login_required
@user_passes_test(lambda u: u.is_superuser)
def edit_therapist(request, pk):
    therapist = get_object_or_404(Therapist, pk=pk)
    form = TherapistForm(instance=therapist)
    return render(request, 'main/edit_therapist.html', {'form': form, 'therapist': therapist})

@login_required
@require_POST
@user_passes_test(lambda u: u.is_superuser)
def update_therapist(request, pk):
    therapist = get_object_or_404(Therapist, pk=pk)
    form = TherapistForm(request.POST, instance=therapist)
    if form.is_valid():
        form.save()
        return redirect('therapist-detail', pk=therapist.pk)
    return render(request, 'main/edit_therapist.html', {'form': form, 'therapist': therapist})

@login_required
@require_POST
@user_passes_test(lambda u: u.is_superuser)
def delete_therapist(request, pk):
    therapist = get_object_or_404(Therapist, pk=pk)
    therapist.delete()
    return redirect('therapists-list')

@login_required
def edit_daily_goal(request, pk):
    goal = get_object_or_404(DailyGoal, pk=pk, user=request.user)
    form = DailyGoalForm(instance=goal)
    return render(request, 'main/edit_daily_goal.html', {'form': form, 'goal': goal})

@login_required
@require_POST
def update_daily_goal(request, pk):
    goal = get_object_or_404(DailyGoal, pk=pk, user=request.user)
    form = DailyGoalForm(request.POST, instance=goal)
    if form.is_valid():
        form.save()
        return redirect('daily-goal-detail', pk=goal.pk)
    return render(request, 'main/edit_daily_goal.html', {'form': form, 'goal': goal})

@login_required
@require_POST
def delete_daily_goal(request, pk):
    goal = get_object_or_404(DailyGoal, pk=pk, user=request.user)
    goal.delete()
    return redirect('daily-goals')

@login_required
def edit_mood_entry(request, pk):
    mood_entry = get_object_or_404(MoodEntry, pk=pk, user=request.user)
    form = MoodEntryForm(instance=mood_entry)
    return render(request, 'main/edit_mood_entry.html', {'form': form, 'mood_entry': mood_entry})

@login_required
@require_POST
def update_mood_entry(request, pk):
    mood_entry = get_object_or_404(MoodEntry, pk=pk, user=request.user)
    form = MoodEntryForm(request.POST, instance=mood_entry)
    if form.is_valid():
        form.save()
        return redirect('mood-entry-detail', pk=mood_entry.pk)
    return render(request, 'main/edit_mood_entry.html', {'form': form, 'mood_entry': mood_entry})

@login_required
@require_POST
def delete_mood_entry(request, pk):
    mood_entry = get_object_or_404(MoodEntry, pk=pk, user=request.user)
    mood_entry.delete()
    return redirect('mood-entries')

