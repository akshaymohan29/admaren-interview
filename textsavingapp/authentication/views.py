from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.exceptions import AuthenticationFailed 
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .models import User
from .serializer import UserRegistrationSerializer

class UserRegistrationView(APIView):
    permission_classes = []

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            email = serializer.validated_data.get('email')
            name =serializer.validated_data.get('name')
            password = serializer.validated_data.get('password')
            User.objects.create_user(email=email, password=password, name=name)
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




from rest_framework_simplejwt.tokens import RefreshToken


class LoginView(APIView):
    permission_classes = []
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        print(email)
        user=User.objects.filter(email=email).first()
        print(user,'usissod')
        if user is  None:
            raise AuthenticationFailed("no user exist")
        if not user.check_password(password):
             raise AuthenticationFailed("check passwd")
        
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_200_OK)
        
