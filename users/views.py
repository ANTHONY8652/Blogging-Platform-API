
from .models import Profile
from django.contrib.auth import get_user_model, authenticate
from .serializers import UserSerializer, UserLoginSerializer, UserLogoutSerializer, ProfileSerialzier
from rest_framework import generics, status, permissions, viewsets
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password

User = get_user_model()

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        if User.objects.filter(email=email).exists():
            return Response({'detail': 'User with this email already exists try using another email address.'})
        
        user = User(
            username = username,
            email = email,
            password = make_password(password)
        )

        user.save()

        token, _ = Token.objects.get_or_create(user=user)

        return Response({
            'user': UserSerializer(user).data,
            'token': token.key,
            'redirect_url': 'http://localhost:8000/api/users/login/'
        }, status=status.HTTP_201_CREATED)

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class UserLoginView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(sel, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(email=email, password=password)

        if user is not None:
            token, _ = Token.objects.get_or_create(user=user)

            return Response({
                'user': UserSerializer(user).data,
                'token': token.key,
                'redirect_url': 'http://localhost:8000/api/events/',
            })
        
        return Response({'detail': 'Invalid email or password'}, status=status.HTTP_400_BAD_REQUEST)


class UserLogoutView(generics.GenericAPIView):
    serializer_class = UserLogoutSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            token = request.auth
            token.delete()

            return Response({
                'message': 'Successfully logget out sad to see you go.',
                'redirect_url': 'http://localhost:8000/api/users/login/',
            }, status=status.HTTP_204_NO_CONTENT)
        
        except (AttributeError, Token.DoesNotExist):
            return Response({'detail': 'Token not found or already logged out, Try again.'}, status=status.HTTP_400_BAD_REQUEST)

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerialzier
    permission_classes = permissions.IsAuthenticatedOrReadOnly

# Create your views here.
