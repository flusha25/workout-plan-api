from django.urls import path, include
from . import views
from .views import TestView
from rest_framework.routers import DefaultRouter
from .views import ExerciseViewSet, GoalViewSet, TokenRefreshAPIView, get_workout_plan_exercises, user_tracking, WorkoutPlanViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="training and exercises",
        default_version='v1',
        description="my api for sweeft",
        contact=openapi.Contact(email="megrelishvili_luka@yahoo.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


router = DefaultRouter()
router.register(r'exercises', ExerciseViewSet, basename='exercises')
router.register(r'workout-plans', WorkoutPlanViewSet, basename='workoutplan')
router.register(r'goals', GoalViewSet,basename='goals' )


urlpatterns = [
    path('register/', views.RegistrationAPIView.as_view(), name='register'),
    path('login/', views.LoginAPIView.as_view(), name='login'),
    path('logout/', views.LogoutAPIView.as_view(), name='logout'),
    path('token/refresh/', TokenRefreshAPIView.as_view(), name='token_refresh'),
    path('test/', TestView.as_view(), name='test-view'),
    path('workout-plan-exercises/', get_workout_plan_exercises, name='get_workout_plan_exercises'),
    path('usertracking/', user_tracking , name='usertracking'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('', include(router.urls))
]