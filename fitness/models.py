
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import Permission, Group
from django.utils.translation import gettext_lazy as _



# dis modl represents  type of phisical activity

class CustomUser(AbstractUser):

    class Meta:
        verbose_name = 'Custom User'
        verbose_name_plural = 'Custom Users'

    # Example of related_name arguments to resolve clashes
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        related_name='custom_user_groups',
        related_query_name='custom_user_group',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='custom_user_permissions',
        related_query_name='custom_user_permission',
    )
class Exercise(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    instructions = models.TextField()
    target_muscles = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
# here is model represent a plan for phisical activities
class WorkoutPlan(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    workout_frequency = models.CharField(max_length=50)
    goals = models.ManyToManyField('Goal')
    exercises = models.ManyToManyField('Exercise', through='WorkoutPlanExercise')#  activities included in this plan

    def __str__(self):
        return self.name
    
# dis model represent a specific activity in a workout plan
class WorkoutPlanExercise(models.Model):
    workout_plan = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    repetitions = models.IntegerField(default=0)
    sets = models.IntegerField(default=0)
    duration = models.DurationField(blank=True, null=True)
    distance = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.workout_plan.name} - {self.exercise.name}"

class Tracking(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    recorded_date = models.DateField()
    weight = models.FloatField()

    def __str__(self):
        return f"{self.user.username} - {self.recorded_date}"

class Goal(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"