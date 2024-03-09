# Generated by Django 5.0.3 on 2024-03-09 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0002_goal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workoutplan',
            name='goals',
        ),
        migrations.AddField(
            model_name='workoutplan',
            name='goals',
            field=models.ManyToManyField(to='fitness.goal'),
        ),
    ]