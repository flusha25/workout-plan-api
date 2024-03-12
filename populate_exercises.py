from django.core.management.base import BaseCommand
from .fitness.models import Exercise
import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wotkoutplan.settings")
django.setup()

def populate_exercises():
    exercises_data = [
            {
                'name': 'Push-ups',
                'description': 'Push-ups are a basic bodyweight exercise that strengthens the chest, shoulders, and triceps.',
                'instructions': '1. Start in a plank position with your hands slightly wider than shoulder-width apart. \n2. Lower your body until your chest nearly touches the floor. \n3. Push yourself back up to the starting position.',
                'target_muscles': 'Chest, Shoulders, Triceps'
            },
            {
                'name': 'Squats',
                'description': 'Squats are a compound exercise that works multiple muscle groups including the quadriceps, hamstrings, and glutes.',
                'instructions': '1. Stand with your feet shoulder-width apart. \n2. Bend your knees and hips to lower your body down as if you are sitting back into a chair. \n3. Keep your chest up and your weight on your heels. \n4. Push through your heels to return to the starting position.',
                'target_muscles': 'Quadriceps, Hamstrings, Glutes'
            },
            {
                'name': 'Pull-ups',
                'description': 'Pull-ups are an upper-body strength exercise that targets the back, shoulders, and arms.',
                'instructions': '1. Grip a pull-up bar with your palms facing away from you, slightly wider than shoulder-width apart. \n2. Hang from the bar with your arms fully extended. \n3. Pull your body up until your chin clears the bar. \n4. Lower yourself back down with control.',
                'target_muscles': 'Back, Shoulders, Biceps'
            },
            {
                'name': 'Deadlifts',
                'description': 'Deadlifts are a compound exercise that targets multiple muscle groups including the back, glutes, and hamstrings.',
                'instructions': '1. Stand with your feet hip-width apart and a barbell in front of you. \n2. Bend at the hips and knees to lower your body down and grasp the bar with an overhand grip. \n3. Keep your back straight and lift the bar by extending your hips and knees. \n4. Lower the bar back down with control.',
                'target_muscles': 'Back, Glutes, Hamstrings'
            },
            {
                'name': 'Bench Press',
                'description': 'The bench press is a compound exercise that primarily targets the chest, shoulders, and triceps.',
                'instructions': '1. Lie flat on a bench with your feet planted on the ground. \n2. Grip the barbell with your hands slightly wider than shoulder-width apart. \n3. Lower the barbell down to your chest, keeping your elbows at a 90-degree angle. \n4. Press the barbell back up to the starting position.',
                'target_muscles': 'Chest, Shoulders, Triceps'
            },
            {
                'name': 'Lunges',
                'description': 'Lunges are a lower-body exercise that targets the quadriceps, hamstrings, and glutes.',
                'instructions': '1. Stand with your feet hip-width apart. \n2. Take a step forward with one foot and lower your body down until both knees are bent at a 90-degree angle. \n3. Push through your front heel to return to the starting position. \n4. Repeat on the other side.',
                'target_muscles': 'Quadriceps, Hamstrings, Glutes'
            },
            {
                'name': 'Plank',
                'description': 'The plank is a core-strengthening exercise that targets the abdominals, back, and shoulders.',
                'instructions': '1. Start in a push-up position with your hands directly under your shoulders. \n2. Engage your core and hold your body in a straight line from head to heels. \n3. Keep your abs tight and avoid sagging or arching your back. \n4. Hold for the desired duration.',
                'target_muscles': 'Abdominals, Back, Shoulders'
            },
            {
                'name': 'Russian Twist',
                'description': 'The Russian twist is a core exercise that targets the obliques and abdominals.',
                'instructions': '1. Sit on the floor with your knees bent and feet flat on the ground. \n2. Lean back slightly and lift your feet off the ground. \n3. Hold your hands together in front of you and twist your torso to one side. \n4. Twist your torso to the other side, moving your hands across your body. \n5. Repeat for the desired number of repetitions.',
                'target_muscles': 'Obliques, Abdominals'
            },
            {
                'name': 'Dumbbell Shoulder Press',
                'description': 'The dumbbell shoulder press is a shoulder-strengthening exercise that targets the deltoid muscles.',
                'instructions': '1. Sit on a bench with back support and hold a dumbbell in each hand at shoulder level. \n2. Press the dumbbells overhead until your arms are fully extended. \n3. Lower the dumbbells back down to shoulder level. \n4. Repeat for the desired number of repetitions.',
                'target_muscles': 'Shoulders'
            },
            {
                'name': 'Bicep Curls',
                'description': 'Bicep curls are an isolation exercise that targets the biceps muscles.',
                'instructions': '1. Stand with your feet shoulder-width apart and hold a dumbbell in each hand with palms facing forward. \n2. Curl the dumbbells up towards your shoulders while keeping your elbows close to your sides. \n3. Lower the dumbbells back down to the starting position. \n4. Repeat for the desired number of repetitions.',
                'target_muscles': 'Biceps'
            },
            {
                'name': 'Tricep Dips',
                'description': 'Tricep dips are a bodyweight exercise that targets the triceps muscles.',
                'instructions': '1. Sit on the edge of a sturdy chair or bench with your hands placed next to your hips. \n2. Slide your hips off the edge of the chair and lower your body down by bending your elbows. \n3. Push yourself back up to the starting position by straightening your arms. \n4. Repeat for the desired number of repetitions.',
                'target_muscles': 'Triceps'
            },
            {
                'name': 'Leg Press',
                'description': 'The leg press is a lower-body exercise that primarily targets the quadriceps muscles.',
                'instructions': '1. Sit on a leg press machine with your back flat against the backrest and your feet shoulder-width apart on the footplate. \n2. Press the footplate away from your body by straightening your legs. \n3. Bend your knees and lower the footplate back down towards your body. \n4. Repeat for the desired number of repetitions.',
                'target_muscles': 'Quadriceps'
            },
            {
                'name': 'Plank Jacks',
                'description': 'Plank jacks are a variation of the plank exercise that also targets the cardiovascular system.',
                'instructions': '1. Start in a plank position with your hands directly under your shoulders and your feet together. \n2. Jump your feet out to the sides while keeping your upper body stable. \n3. Jump your feet back together to return to the starting position. \n4. Repeat for the desired number of repetitions.',
                'target_muscles': 'Abdominals, Legs, Cardiovascular system'
            },
            {
                'name': 'Mountain Climbers',
                'description': 'Mountain climbers are a full-body exercise that targets the core, shoulders, and legs.',
                'instructions': '1. Start in a push-up position with your hands directly under your shoulders. \n2. Drive one knee towards your chest and then quickly switch legs, alternating back and forth. \n3. Keep your hips low and your core engaged throughout the movement. \n4. Repeat for the desired number of repetitions.',
                'target_muscles': 'Abdominals, Shoulders, Legs'
            },
            {
                'name': 'Burpees',
                'description': 'Burpees are a full-body exercise that combines a squat, push-up, and jump.',
                'instructions': '1. Start in a standing position with your feet shoulder-width apart. \n2. Squat down and place your hands on the ground in front of you. \n3. Jump your feet back into a plank position and perform a push-up. \n4. Jump your feet back towards your hands and explode upwards into a jump. \n5. Land softly and immediately lower back down into the next repetition.',
                'target_muscles': 'Full body'
            },
            {
                'name': 'Crunches',
                'description': 'Crunches are an abdominal exercise that targets the rectus abdominis muscles.',
                'instructions': '1. Lie on your back with your knees bent and feet flat on the ground. \n2. Place your hands behind your head or across your chest. \n3. Lift your shoulders off the ground by contracting your abdominal muscles. \n4. Lower your shoulders back down to the starting position.',
                'target_muscles': 'Abdominals'
            },
            {
                'name': 'Hammer Curls',
                'description': 'Hammer curls are a variation of bicep curls that target the biceps and brachialis muscles.',
                'instructions': '1. Stand with your feet shoulder-width apart and hold a dumbbell in each hand with palms facing your body. \n2. Curl the dumbbells up towards your shoulders while keeping your palms facing each other. \n3. Lower the dumbbells back down to the starting position. \n4. Repeat for the desired number of repetitions.',
                'target_muscles': 'Biceps, Brachialis'
            },
            {
                'name': 'Russian Twist',
                'description': 'The Russian twist is a core-strengthening exercise that targets the obliques and abdominals.',
                'instructions': '1. Sit on the floor with your knees bent and feet flat on the ground. \n2. Lean back slightly and lift your feet off the ground. \n3. Hold your hands together in front of you and twist your torso to one side. \n4. Twist your torso to the other side, moving your hands across your body. \n5. Repeat for the desired number of repetitions.',
                'target_muscles': 'Obliques, Abdominals'
            },
            {
                'name': 'Reverse Lunges',
                'description': 'Reverse lunges are a variation of lunges that target the quadriceps, hamstrings, and glutes.',
                'instructions': '1. Stand with your feet hip-width apart and hands on your hips. \n2. Take a step back with one foot and lower your body down until both knees are bent at a 90-degree angle. \n3. Push through your front heel to return to the starting position. \n4. Repeat on the other side.',
                'target_muscles': 'Quadriceps, Hamstrings, Glutes'
            },
            {
                'name': 'Side Plank',
                'description': 'The side plank is a variation of the plank exercise that targets the obliques and abdominals.',
                'instructions': '1. Start in a plank position with your hands directly under your shoulders. \n2. Rotate your body to one side and balance on one forearm and the side of your foot. \n3. Keep your body in a straight line from head to heels. \n4. Hold for the desired duration and repeat on the other side.',
                'target_muscles': 'Obliques, Abdominals'
            },
            {
                'name': 'Leg Raises',
                'description': 'Leg raises are a core-strengthening exercise that targets the lower abdominals.',
                'instructions': '1. Lie on your back with your legs straight and your hands by your sides. \n2. Lift your legs off the ground by contracting your lower abdominals. \n3. Keep your legs straight as you raise them towards the ceiling. \n4. Lower your legs back down to the starting position with control.',
                'target_muscles': 'Lower abdominals'
            },
            {
                'name': 'Dumbbell Lunges',
                'description': 'Dumbbell lunges are a variation of lunges that target the quadriceps, hamstrings, and glutes.',
                'instructions': '1. Stand with your feet hip-width apart and hold a dumbbell in each hand by your sides. \n2. Take a step forward with one foot and lower your body down until both knees are bent at a 90-degree angle. \n3. Push through your front heel to return to the starting position. \n4. Repeat on the other side.',
                'target_muscles': 'Quadriceps, Hamstrings, Glutes'
            },
            {
                'name': 'Flutter Kicks',
                'description': 'Flutter kicks are a core-strengthening exercise that targets the lower abdominals.',
                'instructions': '1. Lie on your back with your legs straight and your hands under your glutes for support. \n2. Lift your legs off the ground a few inches and alternate kicking them up and down in a fluttering motion. \n3. Keep your lower back pressed into the ground and your core engaged throughout the movement. \n4. Repeat for the desired number of repetitions.',
                'target_muscles': 'Lower abdominals'
            },
        ]

    for exercise_data in exercises_data:
        exercise = Exercise.objects.create(**exercise_data)
        print(f'Exercise created: {exercise}')

        
if __name__ == "__main__":
    populate_exercises()
'''
# fitness/management/commands/insert_goals.py
import json
from django.core.management.base import BaseCommand
from fitness.models import Exercise, Goal

class Command(BaseCommand):
    help = 'Inserts goals from JSON data into the database'

    def handle(self, *args, **options):
        goals_data = [
            {"name": "Muscle Building", "description": "Users may have a goal to increase muscle mass and strength in specific muscle groups."},
            {"name": "Weight Loss", "description": "Users may aim to lose weight and reduce body fat percentage."},
            {"name": "Endurance Training", "description": "Users may want to improve cardiovascular endurance and stamina for activities like running or cycling."},
            {"name": "Flexibility Improvement", "description": "Users may focus on increasing flexibility and mobility through stretching exercises."},
            {"name": "Functional Strength", "description": "Users may prioritize exercises that improve functional strength for daily activities."},
            {"name": "Sports-Specific Training", "description": "Users may have goals related to enhancing performance in a specific sport or activity."},
            {"name": "Injury Rehabilitation", "description": "Users recovering from injuries may have rehabilitation goals to regain strength and mobility."}
        ]

        for goal_data in goals_data:
            Goal.objects.create(name=goal_data['name'], description=goal_data['description'])

        self.stdout.write(self.style.SUCCESS('Goals inserted successfully'))
'''