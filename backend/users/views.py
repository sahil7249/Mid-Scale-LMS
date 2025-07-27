from .serializer import UserSerialzer
from .models import User
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class RegisterUserView(APIView):

    def post(self,request):
        serializer = UserSerialzer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(UserSerialzer(user).data,status=status.HTTP_200_OK)
    
class UserView(APIView):
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