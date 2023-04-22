from rest_framework import serializers
import datetime

from .models import Courses, Students

# For showing the students who matched for the course instance in the view
class CourseStudentSerializer(serializers.ModelSerializer):

    students = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Courses
        fields = (
            "id",
            "course_name",
            "students",
        )

# For showing the courses which the student takes
class CoursesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Courses
        fields = (
            "id",
            "course_name",
        )

# for listing all students 
class StudentsListSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField()
    user_id = serializers.IntegerField()
    courses = CoursesSerializer(many=True)

    class Meta:
        model = Students
        fields = (
            "id",
            "user",
            "user_id",
            "first_name",
            "last_name",
            "dob",
            "courses",
        )

# for student create, update and delete
class StudentsSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField()
    user_id = serializers.IntegerField()

    class Meta:
        model = Students
        fields = (
            "id",
            "user",
            "user_id",
            "first_name",
            "last_name",
            "dob",
            "courses",
        )