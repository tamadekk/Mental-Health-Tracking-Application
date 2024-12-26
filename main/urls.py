from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('accounts/logout/', views.user_logout, name='logout'),
    path('manage-users/', views.manage_users, name='manage_users'),
    path('mood-entries/', views.MoodEntryListView.as_view(), name='mood-entries'),
    path('mood-entry/<int:pk>/', views.MoodEntryDetailView.as_view(), name='mood-entry-detail'),
    path('add-mood-entry/', views.add_mood_entry, name='add-mood-entry'),
    path('mood-entry/edit/<int:pk>/', views.edit_mood_entry, name='edit-mood-entry'),
    path('mood-entry/update/<int:pk>/', views.update_mood_entry, name='update-mood-entry'),
    path('mood-entry/delete/<int:pk>/', views.delete_mood_entry, name='delete-mood-entry'),
    path('daily-goals/', views.DailyGoalListView.as_view(), name='daily-goals'),
    path('daily-goal/<int:pk>/', views.DailyGoalDetailView.as_view(), name='daily-goal-detail'),
    path('add-daily-goal/', views.add_daily_goal, name='add-daily-goal'),
    path('daily-goal/edit/<int:pk>/', views.edit_daily_goal, name='edit-daily-goal'),
    path('daily-goal/update/<int:pk>/', views.update_daily_goal, name='update-daily-goal'),
    path('daily-goal/delete/<int:pk>/', views.delete_daily_goal, name='delete-daily-goal'),
    path('goals/', views.view_goals, name='view-goals'),
    path('therapists-list/', views.TherapistListView, name='therapists-list'),
    path('therapist/<int:pk>/', views.TherapistDetailView, name='therapist-detail'),
    path('therapist/edit/<int:pk>/', views.edit_therapist, name='edit-therapist'),
    path('therapist/update/<int:pk>/', views.update_therapist, name='update-therapist'),
    path('therapist/delete/<int:pk>/', views.delete_therapist, name='delete-therapist'),
]