from django.contrib import admin

from .models import (
    Platform,
    Game,
    Match,
    Round,
    Stage,
    MatchParticipant,
    Tournament,
    TrophyCategory,
    BadgesCategory,
    UserTrophyCase,
    UserMatchParticipant,
    UserPlatform,
    UserGame,
)


class PlatformAdmin(admin.ModelAdmin):
    list_display = ('name', 'manufacturer', 'get_games')


class GameAdmin(admin.ModelAdmin):
    list_display = ('display_name', 'get_platforms',)


# class TrophyCaseAdmin(admin.ModelAdmin):
#     list_display = ('user_id', 'plateform', 'game', 'match', 'badges_category',)

class UserPlatformAdmin(admin.ModelAdmin):
    list_display = ['user_id']


admin.site.register(UserPlatform, UserPlatformAdmin)


class UserGameAdmin(admin.ModelAdmin):
    list_display = ['gammer_tag']


admin.site.register(UserGame, UserGameAdmin)


class UserMatchParticipantAdmin(admin.ModelAdmin):
    list_display = ['usermatchparticipant_id']


admin.site.register(UserMatchParticipant, UserMatchParticipantAdmin)

admin.site.register(Tournament)
admin.site.register(Platform, PlatformAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Match)
admin.site.register(MatchParticipant)
admin.site.register(Round)
admin.site.register(Stage)
admin.site.register(UserTrophyCase)
admin.site.register(TrophyCategory)
admin.site.register(BadgesCategory)

