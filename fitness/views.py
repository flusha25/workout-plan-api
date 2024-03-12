# Import necessary modules and components
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User
from .serializers import CustomUserSerializer, ExerciseSerializer, WorkoutPlanSerializer, TrackingSerializer, GoalSerializer, WorkoutPlanExerciseSerializer
from rest_framework.permissions import IsAuthenticated
from . permissions import ReadOnlyPermission
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Exercise, WorkoutPlan, Tracking, Goal, CustomUser, WorkoutPlanExercise
from rest_framework import viewsets


# Define viewsets for CRUD operations on different models
class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = [IsAuthenticated,ReadOnlyPermission]


class GoalViewSet(viewsets.ModelViewSet):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer
    permission_classes = [IsAuthenticated]

class WorkoutPlanViewSet(viewsets.ModelViewSet):
    queryset = WorkoutPlan.objects.all()
    serializer_class = WorkoutPlanSerializer

    def list(self, request):
        queryset = self.queryset.filter(user=request.user)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Define a function-based view to get workout plan exercises associated with the requesting user
@api_view(['GET'])
def get_workout_plan_exercises(request):
    """
    Retrieve workout plan exercises associated with the requesting user.

    Only returns workout plan exercises if the user is authenticated.
    """
    if request.method == 'GET':
        user = request.user
        if user.is_authenticated:
            workout_plan_exercises = WorkoutPlanExercise.objects.filter(workout_plan__user=user)
            serializer = WorkoutPlanExerciseSerializer(workout_plan_exercises, many=True)
            return Response(serializer.data)
        else:
            return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)


# Define JWT-related handlers
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

@api_view(['GET', 'POST','PATCH'])
@permission_classes([IsAuthenticated])
def user_tracking(request):
    """
    Retrieve tracking records associated with the requesting user (GET) or create a new tracking record (POST).
    """
    if request.method == 'GET':
        user = request.user
        if user.is_authenticated:
            user_tracking = Tracking.objects.filter(user=user)
            serializer = TrackingSerializer(user_tracking, many=True)
            return Response(serializer.data)
        else:
            return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)
    elif request.method == 'POST':
        serializer = TrackingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Define a test view to check authentication
class TestView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({"message": f"Hello, {user.username}! You're authenticated."})


# Define API views for user registration, token refresh, user login, and user logout
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
    
class TokenRefreshAPIView(APIView):
    def post(self, request):
        refresh_token = request.data.get('refresh_token')

        if not refresh_token:
            return Response({'error': 'Refresh token is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            refresh_token = RefreshToken(refresh_token)
            access_token = str(refresh_token.access_token)
            return Response({'access_token': access_token}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': 'Invalid refresh token'}, status=status.HTTP_400_BAD_REQUEST)

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
