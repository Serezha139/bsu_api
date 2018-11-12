from django.db import models

# Create your models here.


class Player(models.Model):
    first_name = models.fields.CharField(max_length=20)
    last_name = models.fields.CharField(max_length=20)
    photo = models.ImageField(blank=True)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)


class Team(models.Model):
    name = models.CharField(max_length=50)
    players = models.ManyToManyField(Player, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.name


