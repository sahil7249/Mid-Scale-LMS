from django.shortcuts import render
from .serializer import UserSerialzer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class RegisterUserView(APIView):
    def get(self,request):
        return Response('Register User view',status=200)

    def post(self,request):
        serializer = UserSerialzer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(UserSerialzer(user).data,status=status.HTTP_200_OK)
    


