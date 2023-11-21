from django.urls import path

from tasks.apps import TasksConfig
from tasks.views import TaskCreateAPIView, TaskListAPIView, TaskRetrieveAPIView, TaskUpdateAPIView, TaskDestroyAPIView

app_name = TasksConfig.name

urlpatterns = [
    path('create/', TaskCreateAPIView.as_view(), name='tasks-create'),
    path('', TaskListAPIView.as_view(), name='tasks-list'),
    path('<int:pk>/', TaskRetrieveAPIView.as_view(), name='tasks-retrieve'),
    path('edit/<int:pk>/', TaskUpdateAPIView.as_view(), name='tasks-update'),
    path('delete/<int:pk>/', TaskDestroyAPIView.as_view(), name='tasks-delete'),
]
