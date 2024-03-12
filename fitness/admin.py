from django.contrib import admin
from .models import Exercise, WorkoutPlan, WorkoutPlanExercise, Tracking, Goal

admin.site.register(Exercise)
admin.site.register(WorkoutPlan)
admin.site.register(WorkoutPlanExercise)
admin.site.register(Tracking)
admin.site.register(Goal)