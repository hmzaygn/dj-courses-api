from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import CoursesMVS, StudentsListView, StudentsMVS

router = DefaultRouter()
router.register("courses", CoursesMVS)
router.register("students", StudentsMVS)


urlpatterns = [
    path("students-list/", StudentsListView.as_view()),
] + router.urls
