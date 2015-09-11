from rest_framework import serializers
from .models import Noticias

class NoticiasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noticias
        fields = ('id', 'titulo', 'slug', 'fecha', 'foto', 'url', 'texto', 'categoria', 'user')
