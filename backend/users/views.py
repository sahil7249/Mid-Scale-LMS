from .serializer import UserSerialzer
from .models import User
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

class RegisterUserView(APIView):
    def post(self,request):
        serializer = UserSerialzer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(UserSerialzer(user).data,status=status.HTTP_200_OK)

class UserLoginView(APIView):
    def post(self,request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username,password=password)
        if user is not None :
            refresh_token = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh_token),
                'access': str(refresh_token.access_token),
                'role':user.role,
                'username':user.username
            })
        else:
            return Response({"detail":"Invalid credentials"},status=status.HTTP_404_NOT_FOUND)

        

class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request,pk=None):
        user = User.objects.get(pk=pk)
        serializer = UserSerialzer(user)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,pk=None):
        user_data = get_object_or_404(User,pk=pk)
        serializer = UserSerialzer(user_data,data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(UserSerialzer(user).data,status=status.HTTP_200_OK)