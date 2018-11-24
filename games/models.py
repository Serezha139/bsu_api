from django.db import models
from teams.models import Team

STAGE_CHOICES = (
    ("FEST", "Фестиваль"),
    ("CUP", "Кубок"),
    ("ONE_EIGHT", "Одна Восьмая"),
    ("QUATERFINAL", "Одна Четвертая"),
    ("SEMIFINAL", "Полуфинал"),
    ("FINAL", "Финал"),
)

SEASON_CHOICES = (
    (2018, '2018'),
    (2019, '2019')
)

STATUS_CHOICES = (
    ('LIVE', 'Live'),
    ('FINISHED', 'Finished'),
    ('UPCOMING', 'Upcoming')
)


class Game(models.Model):
    game_datetime = models.fields.DateTimeField()
    teams = models.ManyToManyField(Team)
    stage = models.fields.CharField(choices=STAGE_CHOICES, max_length=40)
    description = models.fields.TextField()
    season = models.fields.IntegerField(choices=SEASON_CHOICES, null=True)
    status = models.fields.CharField(
        choices=STATUS_CHOICES,
        max_length=40,
        default='UPCOMING'
    )

    def __str__(self):
        return "%s %s %s" % (
            str(self.season),
            self.get_stage_display(),
            str(self.game_datetime.date())
        )
