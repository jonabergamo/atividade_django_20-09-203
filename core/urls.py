from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from drf_yasg import openapi
from api.views import (
    StudentDetailUpdateDeleteAPIView,
    StudentListCreateAPIView,
    SubjectDetailUpdateDeleteAPIView,
    SubjectListCreateAPIView,
    TaskDetailUpdateDeleteAPIView,
    TaskListCreateAPIView,
    StudentTaskListAPIView,
)

# Schema View for API documentation
schema_view = get_schema_view(
    openapi.Info(
        title="Student Task and Discipline Management API",  # Title of the API
        default_version="v1",  # Default API version
        description="""This API aims to help students manage their disciplines and tasks.
                       It offers secured endpoints for creating, updating, and deleting both disciplines and tasks.
                       It also maintains the relationships between these entities and applies necessary validations.""",
        contact=openapi.Contact(email="jonathanbergamo16@gmail.com"),  # Contact Information
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),  # Public API with AllowAny permission
)

# API URL routes
api_routes = [
    path("alunos", StudentListCreateAPIView.as_view()),  # Student listing and creation
    path("alunos/<int:id>/", StudentDetailUpdateDeleteAPIView.as_view()),  # Student details, update, delete
    path("disciplinas", SubjectListCreateAPIView.as_view()),  # Subject listing and creation
    path("disciplinas/<int:id>/", SubjectDetailUpdateDeleteAPIView.as_view()),  # Subject details, update, delete
    path("tarefas", TaskListCreateAPIView.as_view()),  # Task listing and creation
    path("tarefas/<int:id>/", TaskDetailUpdateDeleteAPIView.as_view()),  # Task details, update, delete
    path("alunos/<int:student_id>/tarefas/", StudentTaskListAPIView.as_view()),  # List tasks for a specific student
]

# URL Patterns
urlpatterns = [
    path("admin/", admin.site.urls),  # Admin panel
    path("api/", include(api_routes)),  # API Endpoints
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",  # Swagger UI for API documentation
    ),
]
