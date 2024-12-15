from django.urls import path
from . import views



urlpatterns = [
    path('users/register/', views.RegisterAPIView.as_view()),
    path('users/<int:pk>/', views.UserDetailsAPIView.as_view()),
    path('projects/', views.ProjectListCreateAPIView.as_view()),
    path('projects/<int:pk>/', views.ProjectDetailsAPIView.as_view()),
    path('projects/<int:project_id>/tasks/', views.TaskListCreateAPIView.as_view()),
    path('tasks/<int:pk>/', views.TaskDetailsAPIView.as_view()),
    path('tasks/<int:task_id>/comment/', views.CommentListCreateAPIView.as_view()),
    path('comments/<int:pk>/', views.CommentDetailsAPIView.as_view()),
]


