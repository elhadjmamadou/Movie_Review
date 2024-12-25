from rest_framework import generics
from .models import Film, Critique
from .serializers import FilmSerializer, CritiqueSerializer, CustomUserSerializer
from accounts.models import CustomUser
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class FilmListCreateView(generics.ListCreateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]


class FilmDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    permission_classes = [IsAuthenticated]

class CritiqueListCreateView(generics.ListCreateAPIView):
    queryset = Critique.objects.all()
    serializer_class = CritiqueSerializer
    permission_classes = [IsAuthenticated]

class CritiqueDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Critique.objects.all()
    serializer_class = CritiqueSerializer
    permission_classes = [IsAuthenticated]

class CustomUserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]


class CustomUserDetailView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]