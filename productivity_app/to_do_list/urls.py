from django.urls import path, include

from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('task/', views.task, name='task'),
  path('delete_task/<int:pk>', views.DeleteTask.as_view(), name='delete_task'),
  path('update_task/<int:pk>', views.UpdateTask.as_view(), name='update_task'),
]