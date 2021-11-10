from django.urls import path, include

from . import views

urlpatterns = [
  path('', views.user_profile, name='user_profile'),
  path('login/', views.user_login, name='user_login'),
  path('signup/', views.add_user, name='add_user'),
]