from rest_framework import serializers
from polls.models import Poll


class PollSerializer(serializers.ModelSerializer):
    choices = serializers.StringRelatedField(many=True)

    class Meta:
        model = Poll
        fields = ('id', 'question_text', 'choices')

