from django.contrib import admin

from games.models import Game

# Register your models here.


class GameAdmin(admin.ModelAdmin):
    filter_horizontal = ('teams', )


admin.site.register(Game, GameAdmin)
