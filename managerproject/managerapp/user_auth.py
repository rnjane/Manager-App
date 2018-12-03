from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status

class UserAuth():
    def login(self, username, password):
        user = authenticate(username=username, password=password)
        if user is not None:
            return Response({"message": "succesfully logged in"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Please enter a correct username and password. Note that both fields may be case-sensitive."}, status=status.HTTP_403_FORBIDDEN)
