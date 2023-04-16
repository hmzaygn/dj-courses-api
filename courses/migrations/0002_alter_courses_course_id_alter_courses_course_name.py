# Generated by Django 4.1.6 on 2023-04-16 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='course_id',
            field=models.CharField(max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='courses',
            name='course_name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]