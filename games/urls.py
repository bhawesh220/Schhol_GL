from django.urls import path
from games.views import PlatformAPI, GameAPI, TournamentAPI, StageTypeAPI, StageAPI, GroupAPI, RoundAPI, MatchAPI, \
    MatchParticipantAPI, TrophyCategoryAPI, BadgesCategoryAPI, UserTrophyCaseAPI, UserPlatformAPI, UserGameAPI, UserMatchParticipantAPI

urlpatterns = [
    path('platform/<int:pk>/', PlatformAPI.as_view(), name='platform'),
    path('platform/', PlatformAPI.as_view(), name='platform'),
    path('game/<int:pk>/', GameAPI.as_view(), name='game'),
    path('game/', GameAPI.as_view(), name='game'),
    path('tournament/', TournamentAPI.as_view(), name='tournament'),
    path('stagetype/', StageTypeAPI.as_view(), name='stagetype'),
    path('stage/', StageAPI.as_view(), name='stage'),
    path('group/', GroupAPI.as_view(), name='group'),
    path('round/', RoundAPI.as_view(), name='round'),
    path('match/', MatchAPI.as_view(), name='match'),
    path('matchparticipant/', MatchParticipantAPI.as_view(), name='matchparticipant'),
    path('trophycategory/', TrophyCategoryAPI.as_view(), name='trophycategory'),
    path('trophycategory/', TrophyCategoryAPI.as_view(), name='trophycategory'),
    path('badgescategory/', BadgesCategoryAPI.as_view(), name='BadgesCategory'),
    path('badgescategory/<int:pk>/', BadgesCategoryAPI.as_view(), name='badgescategory'),
    path('usertrophycase/', UserTrophyCaseAPI.as_view(), name='usercasetrophy'),
    path('userplatform/<int:pk>/', UserPlatformAPI.as_view(), name='userplatform'),
    path('userplatform/', UserPlatformAPI.as_view(), name='userplatform'),
    path('usergame/<int:pk>/', UserGameAPI.as_view(), name='usergame'),
    path('usergame/', UserGameAPI.as_view(), name='usergame'),
    path('usermatchparticipants/', UserMatchParticipantAPI.as_view(), name='usermatchparticipants'),

]
