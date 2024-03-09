from django.contrib.auth.models import User
from django.db import models

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    instructions = models.TextField()
    target_muscles = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class WorkoutPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    workout_frequency = models.CharField(max_length=50)
    goals = models.ManyToManyField('Goal')
    exercises = models.ManyToManyField(Exercise, through='WorkoutPlanExercise')

    def __str__(self):
        return self.name

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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recorded_date = models.DateField()
    weight = models.FloatField()

    def __str__(self):
        return f"{self.user.username} - {self.recorded_date}"

class Goal(models.Model):
    name = models.CharField(max_length=100)