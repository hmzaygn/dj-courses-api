from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import Courses, Students
from .serializers import CoursesSerializer, StudentsSerializer

class CoursesMVS(viewsets.ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class StudentsMVS(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
    # permission_classes = [IsAuthenticated, IsAdminUser]
