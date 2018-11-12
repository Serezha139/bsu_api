from django.contrib import admin

from teams.models import Team, Player
# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    filter_horizontal = ('players', )


admin.site.register(Team, TeamAdmin)
admin.site.register(Player)
