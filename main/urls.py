from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('accounts/logout/', views.user_logout, name='logout'),
    path('manage-users/', views.manage_users, name='manage_users'),
    path('mood-entries/', views.mood_entries, name='mood-entries'),
    path('add-mood-entry/', views.add_mood_entry, name='add-mood-entry'),
    path('daily-goals/', views.daily_goals, name='daily-goals'),
    path('add-daily-goal/', views.add_daily_goal, name='add-daily-goal'),
    path('goals/', views.view_goals, name='view-goals'),
    path('therapists-list/', views.therapists_list, name='therapists-list'),
]