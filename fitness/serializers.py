
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Exercise, WorkoutPlan, WorkoutPlanExercise, Tracking, Goal

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['id', 'username','password', 'email', 'first_name', 'last_name'] 

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = User(**validated_data)
        if password is not None:
            user.set_password(password)
        user.save()
        return user    
    

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ['id', 'name', 'description', 'instructions', 'target_muscles']

class WorkoutPlanExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutPlanExercise
        fields = ['exercise', 'repetitions', 'sets', 'duration', 'distance']

class WorkoutPlanSerializer(serializers.ModelSerializer):
    exercises = WorkoutPlanExerciseSerializer(many=True)

    class Meta:
        model = WorkoutPlan
        fields = ['id', 'user', 'name', 'workout_frequency', 'goals', 'exercises']

    def create(self, validated_data):
        exercises_data = validated_data.pop('exercises')
        workout_plan = WorkoutPlan.objects.create(**validated_data)
        for exercise_data in exercises_data:
            WorkoutPlanExercise.objects.create(workout_plan=workout_plan, **exercise_data)
        return workout_plan

class TrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tracking
        fields = ['id', 'user', 'recorded_date', 'weight']

class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = ['id', 'name']
