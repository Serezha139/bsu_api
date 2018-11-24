from django.db import models

# Create your models here.
from django.db import models


class Poll(models.Model):
    question_text = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    poll = models.ForeignKey(
        Poll,
        related_name='choices',
        on_delete=models.CASCADE,
        null=True
    )
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
