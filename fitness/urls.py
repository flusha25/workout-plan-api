from django.urls import path
from . import views
from .views import TestView


urlpatterns = [
    path('register/', views.RegistrationAPIView.as_view(), name='register'),
    path('login/', views.LoginAPIView.as_view(), name='login'),
    path('logout/', views.LogoutAPIView.as_view(), name='logout'),
    path('test/', TestView.as_view(), name='test-view'),
]