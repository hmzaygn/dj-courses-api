from rest_framework import viewsets
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import Courses, Students
from .serializers import (
    CoursesSerializer,
    StudentsListSerializer,
    StudentsSerializer
    )

class CoursesMVS(viewsets.ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class StudentsListView(ListAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsListSerializer
    # permission_classes = [IsAuthenticated, IsAdminUser]

class StudentsMVS(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer