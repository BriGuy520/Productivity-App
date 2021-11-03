from django.urls import path, include

from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('task/', views.task, name='task'),
  path('delete_task/<int:pk>', views.delete_task, name='delete_task'),
]