from rest_framework import viewsets
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import Courses, Students
from .serializers import (
    CourseStudentSerializer,
    StudentsListSerializer,
    StudentsSerializer
    )
from .permissions import IsStaffOrReadOnly

# all users read but only admin can perform create,update or delete
class CoursesMVS(viewsets.ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CourseStudentSerializer
    permission_classes = [IsAuthenticated, IsStaffOrReadOnly]

# all users can see the all students
class StudentsListView(ListAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsListSerializer
    permission_classes = [IsAuthenticated]

# for student creating there is a signal. as soon as the user registers the student instance is created in via signal.
# otherwise only admin can create student instance 
class StudentCreateView(CreateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

# admin can see details, update or delete student instance.
# other users can only make this operations for their own profiles
class StudentsDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        queryset = super().get_queryset()

        if self.request.user.is_staff:
            return super().get_queryset()
        else:
            return queryset.filter(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)