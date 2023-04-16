from rest_framework import serializers

from .models import Courses, Students

class CoursesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Courses
        fields = "__all__"
        # fields = (
        #     "id",
        #     "course_id",
        #     "course_name"
        # )

class StudentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Students
        fields = "__all__"