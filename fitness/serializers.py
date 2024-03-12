from datetime import timedelta
from rest_framework import serializers

from .models import Exercise, WorkoutPlan, WorkoutPlanExercise, Tracking, Goal, CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = CustomUser
        fields = ['id', 'username','password', 'email', 'first_name', 'last_name'] 

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = CustomUser(**validated_data)
        if password is not None:
            user.set_password(password)
        user.save()
        return user    



class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = ['id', 'name']


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'

class WorkoutPlanExerciseSerializer(serializers.ModelSerializer):
    exercise = ExerciseSerializer()

    class Meta:
        model = WorkoutPlanExercise
        fields = ['exercise', 'repetitions', 'sets', 'duration', 'distance']
class WorkoutPlanSerializer(serializers.ModelSerializer):
    exercises = WorkoutPlanExerciseSerializer(many=True, source='workoutplanexercise_set')

    class Meta:
        model = WorkoutPlan
        fields = ['user', 'name', 'workout_frequency', 'goals', 'exercises']
        read_only_fields = ['user']

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user if request and hasattr(request, 'user') else None
        validated_data['user'] = user
        exercises_data = validated_data.pop('workoutplanexercise_set')
        goals_data = validated_data.pop('goals')
        workout_plan = WorkoutPlan.objects.create(**validated_data)
        workout_plan.goals.set(goals_data)

        for exercise_data in exercises_data:
            exercise_info = exercise_data.get('exercise', {})  # Get the nested dictionary under 'exercise'
            exercise_name = exercise_info.get('name')  # Get the value of the 'name' key
            if not exercise_name:
                raise serializers.ValidationError("Exercise name not provided.")
            exercise = Exercise.objects.filter(name=exercise_name).first()
            if not exercise:
                raise serializers.ValidationError(f"Exercise with name '{exercise_name}' does not exist.")
            
            # Remove the exercise key from exercise_data before passing it to create()
            exercise_data.pop('exercise', None)

            # Create the WorkoutPlanExercise object with the extracted exercise and remaining data
            WorkoutPlanExercise.objects.create(workout_plan=workout_plan, exercise=exercise, **exercise_data)

        return workout_plan


class TrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tracking
        fields = ['id', 'user', 'recorded_date', 'weight']




