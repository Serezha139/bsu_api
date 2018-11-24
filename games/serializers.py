from rest_framework import serializers
from games.models import Game
from teams.serializers import TeamGameSerializer
from polls.serializers import PollSerializer


class GameSerializer(serializers.ModelSerializer):
    teams = TeamGameSerializer(many=True, read_only=True)
    polls = PollSerializer(many=True)

    class Meta:
        model = Game
        fields = (
            'teams',
            'game_datetime',
            'description',
            'stage',
            'status',
            'polls'
        )

