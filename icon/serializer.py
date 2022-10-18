from IGL_account.models import User
from rest_framework import serializers
from .models import Icon, IconTeam, IconTeamMember



class IconSerializer(serializers.ModelSerializer):
    class Meta:
        model = Icon
        fields = (
            'first_name', 'last_name', 'display_name', 'display_image', 'user',)


class IconTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = IconTeam
        fields = (
            'icon', 'team_name', 'display_image',)


class IconTeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = IconTeamMember
        fields = (
            "user", 'team', 'joined_at', 'left_at',)
