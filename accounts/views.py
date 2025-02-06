from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.views import APIView
from accounts.serializer import RegisterSerializer
from accounts.utilities.token import get_tokens_for_user


class UserRegistrationAPIView(APIView):
  
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = get_tokens_for_user(user) 
            response_data = {
                'token': token,
                'user': serializer.data,  
            }
            
            return Response(response_data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
