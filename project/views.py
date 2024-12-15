from rest_framework import generics
from rest_framework import permissions
from . import models
from project.serializers import UserRegisterSerializer
from project.serializers import UserDetailsSerializer
from project.serializers import ProjectSerializer
from project.serializers import TaskSerializer
from project.serializers import CommentSerializer
from django.contrib.auth import get_user_model




class RegisterAPIView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.AllowAny]


class UserDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserDetailsSerializer
    queryset = get_user_model().objects.all()



class ProjectListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer
    queryset = models.Project.objects.all()

    def list(self, request, *args, **kwargs):
        t = models.Task.objects.all()
        print(t)
        return super().list(request, *args, **kwargs)


class ProjectDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectSerializer
    queryset = models.Project.objects.all()




class TaskListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self, *args, **kwargs):
        project_id = self.kwargs.get('project_id')
        tasks = models.Task.objects.filter(
            project_id=project_id
        )
        return tasks


class TaskDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    queryset = models.Task.objects.all()


class CommentListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self, *args, **kwargs):
        task_id = self.kwargs.get('task_id')
        tasks = models.Comment.objects.filter(
            task_id=task_id
        )
        return tasks

class CommentDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    queryset = models.Comment.objects.all()



