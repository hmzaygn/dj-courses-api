from rest_framework import serializers
import datetime

from .models import Courses, Students

class CoursesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Courses
        fields = (
            "id",
            "course_name",
        )

class StudentsSerializer(serializers.ModelSerializer):

    courses = CoursesSerializer(many=True, read_only=True)

    class Meta:
        model = Students
        fields = (
            "id",
            "first_name",
            "last_name",
            "dob",
            "courses",
        )