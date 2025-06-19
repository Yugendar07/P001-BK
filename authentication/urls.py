from django.urls import path, include
from . import views


urlpatterns = [
    path('userRegistration', views.UserRegistration.as_view(), name='userRegistration'),
    path('loginAsUser', views.LoginAsUser.as_view(), name='loginAsUser'),
]