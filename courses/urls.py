from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import CoursesMVS, StudentsMVS

router = DefaultRouter()
router.register("courses", CoursesMVS)
router.register("students", StudentsMVS)


urlpatterns = [] + router.urls
