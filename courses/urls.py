from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    CoursesMVS,
    StudentsListView,
    StudentCreateView,
    StudentsDetailView
)
router = DefaultRouter()
router.register("courses", CoursesMVS)  # for all CRUD operations related to Courses


urlpatterns = [
    path("students-list/", StudentsListView.as_view()),  # for listing all students
    path("student-create/", StudentCreateView.as_view()), # for creating a student
    path("student-detail/<int:pk>/", StudentsDetailView.as_view()),  # for updating or deleting a student
] + router.urls
