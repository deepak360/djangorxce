from django.shortcuts import render

# Create your views here.
from auth.serializers import MyTokenObtainPairSerializer, RegisterSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import response, decorators, permissions, status


class MyObtainTokenPairView(TokenObtainPairView):
	permission_classes = (AllowAny,)
	serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
	queryset = User.objects.all()
	permission_classes = (AllowAny,)
	serializer_class = RegisterSerializer
	def post(self, request):
		serializer = self.get_serializer(data=request.data)
		if not serializer.is_valid():
			return response.Response(serializer.errors, status.HTTP_400_BAD_REQUEST)      
		user = serializer.save()
		refresh = RefreshToken.for_user(user)
		res = {
			"refresh": str(refresh),
			"access": str(refresh.access_token),
		}
		return response.Response(res, status.HTTP_201_CREATED)
