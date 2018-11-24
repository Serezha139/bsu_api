from django.db import models
from teams.models import Team

STAGE_CHOICES = (
    ("FEST", "Фестиваль"),
    ("CUP", "Кубок"),
    ("8", "Одна Восьмая"),
    ("4", "Одна Четвертая"),
    ("2", "Полуфинал"),
    ("1", "Финал"),
)

SEASON_CHOICES = (
    (2018, '2018'),
    (2019, '2019')
)


class Game(models.Model):
    game_datetime = models.fields.DateTimeField()
    teams = models.ManyToManyField(Team)
    stage = models.fields.CharField(choices=STAGE_CHOICES, max_length=40)
    description = models.fields.TextField()
    season = models.fields.IntegerField(choices=SEASON_CHOICES, null=True)
    ongoing = models.fields.BooleanField(default=False)


    def __str__(self):
        return "%s %s" % (str(self.season), self.get_stage_display())
