from django.shortcuts import render
from rest_framework.views import APIView
from .models import UserAuthentication
from django.contrib.auth.models import User
from rest_framework.response import Response
from .response_helper import success_response, failure_response
from django.contrib.auth import login, authenticate
from django.core.mail import send_mail
from rest_framework.authtoken.models import Token
from datetime import timedelta
from django.utils import timezone

class UserRegistration(APIView):
    def post(self, request):
        data = request.data

        email = data['email'].lower()
        if User.objects.filter(email = email).last():
            return Response(failure_response(None, "User already exists"))

        user_name = data['first_name'] + data.get('last_name', '')

        User.objects.create_user(first_name = data['first_name'], last_name = data.get('last_name', ''),username = user_name, email = email, password = data['password'])

        subject = "Welcome to Paperly!"
        message = f"Hi {user_name},\n\nThank you for registering with Paperly. We’re excited to have you on board!"
        send_mail(subject, message, None, [email])

        return Response (success_response("User created Succesfully"))


class LoginAsUser(APIView):
    def post(self, request):
        data = request.data

        if 'email' in data:
            email = data['email']
            email = email.lower()
        else:
            email = None

        user = User.objects.filter(email=email).first()

        user = authenticate(username=user.username, password=data['password'])

        if not user:
            return Response(failure_response(None, "Invalid email or password"), status=401)

        login(request, user)
        token, _ = Token.objects.get_or_create(user=user)

        userAuthentication = UserAuthentication.objects.create(user=user, refresh_token = token.key, expires_at=timezone.now() + timedelta(days=7),)
        userAuthentication.save()
        
        res = {}
        
        res['name'] = user.first_name
        res['token'] = token.key
        return Response (success_response(res))