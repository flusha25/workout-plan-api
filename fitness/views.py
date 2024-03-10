# views.py

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User
from .serializers import CustomUserSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import ExerciseSerializer, WorkoutPlanSerializer, TrackingSerializer, GoalSerializer
from .models import Exercise, WorkoutPlan, Tracking, Goal
from rest_framework import viewsets


class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    #permission_classes = [IsAuthenticated]

class WorkoutPlanViewSet(viewsets.ModelViewSet):
    queryset = WorkoutPlan.objects.all()
    serializer_class = WorkoutPlanSerializer
    #permission_classes = [IsAuthenticated]

class TrackingViewSet(viewsets.ModelViewSet):
    queryset = Tracking.objects.all()
    serializer_class = TrackingSerializer
    #permission_classes = [IsAuthenticated]

class GoalViewSet(viewsets.ModelViewSet):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer
    permission_classes = [IsAuthenticated]


jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

class TestView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({"message": f"Hello, {user.username}! You're authenticated."})

class RegistrationAPIView(APIView):
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            
            # Generate access and refresh tokens
            refresh = RefreshToken.for_user(user)
            
            return Response({
                'access_token': str(refresh.access_token),
                'refresh_token': str(refresh)
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        # Authenticate the user
        user = authenticate(username=username, password=password)
        
        if user is None:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Generate access and refresh tokens
        refresh = RefreshToken.for_user(user)
        
        return Response({
            'access_token': str(refresh.access_token),
            'refresh_token': str(refresh)
        }, status=status.HTTP_200_OK)

class LogoutAPIView(APIView):
    def post(self, request):
        # JWT tokens are stateless, so there's no need for a logout endpoint with JWT
        return Response(status=status.HTTP_204_NO_CONTENT)
