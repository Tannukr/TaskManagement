# Generated by Django 5.0.2 on 2025-04-05 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Task1', '0002_course_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='credits',
            field=models.IntegerField(default=3),
        ),
    ]
