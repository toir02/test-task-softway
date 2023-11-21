from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from tasks.models import Task
from tasks.paginations import TaskPagination
from tasks.serializers import TaskSerializer


class TaskCreateAPIView(generics.CreateAPIView):
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        new_task = serializer.save(user=self.request.user)
        new_task.user = self.request.user
        new_task.save()


class TaskListAPIView(generics.ListAPIView):
    serializer_class = TaskSerializer
    pagination_class = TaskPagination
    queryset = Task.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('status', 'created_at',)


class TaskRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class TaskUpdateAPIView(generics.UpdateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class TaskDestroyAPIView(generics.DestroyAPIView):
    queryset = Task.objects.all()
