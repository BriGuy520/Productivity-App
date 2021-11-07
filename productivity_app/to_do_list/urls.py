from django.urls import path, include

from . import views

urlpatterns = [
  path('', views.task, name='task'),
  path('add_task/', views.add_task, name='add_task'),
  path('delete_task/<int:pk>', views.DeleteTask.as_view(), name='delete_task'),
  path('update_task/<int:pk>', views.UpdateTask.as_view(), name='update_task'),
]