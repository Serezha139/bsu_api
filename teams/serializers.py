from rest_framework import serializers
from teams.models import Team, Player


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('first_name', 'last_name', 'photo')


class TeamSerializer(serializers.ModelSerializer):
    players = PlayerSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = ('name', 'description', 'players')


class TeamGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('name', 'description')
