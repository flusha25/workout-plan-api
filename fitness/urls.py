from django.urls import path, include
from . import views
from .views import TestView
from rest_framework.routers import DefaultRouter
from .views import ExerciseViewSet, WorkoutPlanViewSet, TrackingViewSet, GoalViewSet, TokenRefreshAPIView, get_workout_plan_exercises

router = DefaultRouter()
router.register(r'exercises', ExerciseViewSet)
router.register(r'workout-plans', WorkoutPlanViewSet)
router.register(r'trackings', TrackingViewSet)
router.register(r'goals', GoalViewSet)


urlpatterns = [
    path('register/', views.RegistrationAPIView.as_view(), name='register'),
    path('login/', views.LoginAPIView.as_view(), name='login'),
    path('logout/', views.LogoutAPIView.as_view(), name='logout'),
    path('token/refresh/', TokenRefreshAPIView.as_view(), name='token_refresh'),
    path('test/', TestView.as_view(), name='test-view'),
    path('workout-plan-exercises/', get_workout_plan_exercises, name='get_workout_plan_exercises'),
    path('', include(router.urls))
]