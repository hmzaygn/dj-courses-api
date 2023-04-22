# Generated by Django 4.1.6 on 2023-04-22 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0013_students_user_alter_students_courses'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='course_id',
            field=models.CharField(blank=True, max_length=6, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='courses',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
