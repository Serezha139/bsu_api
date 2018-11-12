from rest_framework import serializers
from games.models import Game
from teams.serializers import TeamGameSerializer


class GameSerializer(serializers.ModelSerializer):
    teams = TeamGameSerializer(many=True, read_only=True)

    class Meta:
        model = Game
        fields = ('teams', 'game_datetime', 'description')

