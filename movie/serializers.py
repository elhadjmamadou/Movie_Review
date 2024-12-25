from rest_framework import serializers
from .models import Film, Critique
from accounts.models import CustomUser

class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ['id', 'titre', 'synopsis', 'genre', 'date_sortie', 'duree', 'ntmoy']

class CritiqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Critique
        fields = ['id', 'title', 'content', 'note', 'created_at', 'film', 'owner']

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
