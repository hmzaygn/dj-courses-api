from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Students

# create a student instance for the user as soon as the user registers
@receiver(post_save, sender=User)
def create_student(sender, instance, created, **kwargs):
    if created:
        student = Students.objects.create(
            user=instance,
            first_name=instance.first_name,
            last_name=instance.last_name,
            dob=None
        )
        student.save()