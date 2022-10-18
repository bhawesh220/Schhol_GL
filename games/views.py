'''import required Module'''
from rest_framework.response import Response
from .serializer import PlatformSerializer, GameSerializer, TournamentSerializer, StageTypeSerializer, \
    StageSerializer, GroupSerializer, RoundSerializer, MatchSerializer, MatchParticipantSerializer, \
    TrophyCategorySerializer, BadgesCategorySerializer, UserTrophyCaseSerializer, UserPlatformSerializer, \
    UserGameSerializer, UserMatchParticipantSerializer
from .models import Platform, Game, Tournament, StageType, Stage, Group, Round, Match, MatchParticipant, \
    TrophyCategory, BadgesCategory, UserTrophyCase, UserPlatform, UserGame, UserMatchParticipant

from rest_framework import generics


# Create your views here.

class PlatformAPI(generics.GenericAPIView):
    serializer_class = PlatformSerializer

    def post(self, request):
        """Create List of record for BadgesCategory
              :parm request:object to pass to state when request page/url requested the user
              """
        try:
            serializer = PlatformSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data": serializer.data})
        except:
            return Response({"message": "Unable to create the BadgesCategory details"})

    def get(self, request, pk=None):
        """return a list of all BadgesCategory for specfic Trophy
                :parm request:object to pass state,WHEN page/url requested by user.
                parm pk:pass to BadgesCategory id.
                """
        user_id = pk
        try:
            if user_id is not None:
                user = Platform.objects.get(id=user_id)
                serializer = PlatformSerializer(user)
                return Response({"data": serializer.data})
            user = Platform.objects.all()
            serializer = PlatformSerializer(user, many=True)
            return Response({"data": serializer.data})
        except:
            return Response({"message": "Unable to get the BadgesCategory details"})

    def put(self, request, pk=id):
        """update a list of record for BadgesCategory,when request page/url requested the user
                :params pk pass the  BadgesCategory record id"""
        try:
            user_id = pk
            user = Platform.objects.get(id=user_id)
            serializer = PlatformSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg": "plateform badges is updated"})
        except:
            return Response({"message": "Unable to perform the update Badges category details"})

    def delete(self, request, pk):
        """delete a single record for BadgesCategory,when request page/url requested the user
                      :params pk pass the  BadgesCategory record id"""

        plateform = Platform(pk)
        plateform.delete()
        return Response({"msg": "BadgesCategory badges is deleted"})

    def post(self, request):
        serializer = PlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data})

    def delete(self, request, pk):
        platform = Platform(pk)
        platform.delete()
        return Response({"msg": "Platform is deleted"})


class GameAPI(generics.GenericAPIView):
    serializer_class = GameSerializer

    def post(self, request):
        try:
            serializer = GameSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data": serializer.data})
        except Exception as ex:
            print(str(ex))

    def get(self, request, pk=None):
        user_id = pk
        if user_id is not None:
            user = Game.objects.get(id=user_id)
            serializer = GameSerializer(user)
            return Response({"data": serializer.data})
        user = Game.objects.all()
        serializer = GameSerializer(user, many=True)
        return Response({"data": serializer.data})

    def delete(self, request, pk):
        game = Game(pk)
        game.delete()
        return Response({"msg": "game is deleted"})


class TournamentAPI(generics.GenericAPIView):
    serializer_class = TournamentSerializer

    def post(self, request):
        try:
            serializer = TournamentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data": serializer.data})
        except:
            return Response({"message": "Unable to create the Tournament details"})

    def get(self, request, pk=None):
        user_id = pk
        try:
            if user_id is not None:
                user = Tournament.objects.get(id=user_id)
                serializer = TournamentSerializer(user)
                return Response({"data": serializer.data})
            user = Tournament.objects.all()
            serializer = TournamentSerializer(user, many=True)
            return Response({"data": serializer.data})
        except:
            return Response({"message": "No tournament registered"})


class StageTypeAPI(generics.GenericAPIView):
    serializer_class = StageTypeSerializer

    def post(self, request):
        try:
            serializer = StageTypeSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data": serializer.data})
        except Exception as ex:
            print(str(ex))

    def get(self, request, pk=None):
        user_id = pk
        if user_id is not None:
            user = StageType.objects.get(id=user_id)
            serializer = StageTypeSerializer(user)
            return Response({"data": serializer.data})
        user = StageType.objects.all()
        serializer = StageTypeSerializer(user, many=True)
        return Response({"data": serializer.data})


class StageAPI(generics.GenericAPIView):
    serializer_class = StageSerializer

    def post(self, request):
        try:
            serializer = StageSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data": serializer.data})
        except:
            return Response({"message": "Unable to update the Team member registration"})

    def get(self, request, pk=None):
        user_id = pk
        try:
            if user_id is not None:
                user = Stage.objects.get(id=user_id)
                serializer = StageSerializer(user)
                return Response({"data": serializer.data})
            user = Stage.objects.all()
            serializer = StageSerializer(user, many=True)
            return Response({"data": serializer.data})
        except:
            return Response({"message": "Unable to find team member details"})


class GroupAPI(generics.GenericAPIView):
    serializer_class = GroupSerializer

    def post(self, request):
        try:
            serializer = GroupSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data": serializer.data})
        except:
            return Response({"message": "Unable to create group"})

    def get(self, request, pk=None):
        user_id = pk
        try:
            if user_id is not None:
                user = Group.objects.get(id=user_id)
                serializer = GroupSerializer(user)
                return Response({"data": serializer.data})
            user = Group.objects.all()
            serializer = GroupSerializer(user, many=True)
            return Response({"data": serializer.data})
        except:
            return Response({"message": "Unable to get the group details"})


class RoundAPI(generics.GenericAPIView):
    serializer_class = RoundSerializer

    def post(self, request):
        """Create List of record for Round
                      :parm request:object to pass to state when request page/url requested the user
                      """
        try:
            serializer = RoundSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data": serializer.data})
        except:
            return Response({"message": "Unable to define the Round"})

    def get(self, request, pk=None):
        """return a list of all Round for specfic Round
                               :parm request:object to pass state,WHEN page/url requested by user.
                               parm pk:pass to Round id.
                               """
        user_id = pk
        try:
            if user_id is not None:
                user = Round.objects.get(id=user_id)
                serializer = RoundSerializer(user)
                return Response({"data": serializer.data})
            user = Round.objects.all()
            serializer = RoundSerializer(user, many=True)
            return Response({"data": serializer.data})
        except:
            return Response({"message": "Unable to get Round details"})


class MatchAPI(generics.GenericAPIView):
    serializer_class = MatchSerializer

    def post(self, request):
        """Create List of record for Match
                      :parm request:object to pass to state when request page/url requested the user
                      """
        try:
            serializer = MatchSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data": serializer.data})
        except:
            return Response({"message": "Unable to create Matches"})

    def get(self, request, pk=None):
        """return a list of all Match for specfic Match
                       :parm request:object to pass state,WHEN page/url requested by user.
                       parm pk:pass to trophyCategory id.
                       """
        user_id = pk
        try:
            if user_id is not None:
                user = Match.objects.get(id=user_id)
                serializer = MatchSerializer(user)
                return Response({"data": serializer.data})
            user = Match.objects.all()
            serializer = MatchSerializer(user, many=True)
            return Response({"data": serializer.data})
        except:
            return Response({"message": "Unable to get Match details"})


class MatchParticipantAPI(generics.GenericAPIView):
    serializer_class = MatchParticipantSerializer

    def post(self, request):
        """Create List of record for MatchPartipant
              :parm request:object to pass to state when request page/url requested the user
              """
        try:
            serializer = MatchParticipantSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data": serializer.data})
        except:
            return Response({"message": "Unable to create MatchParticipant for Matches"})

    def get(self, request, pk=None):
        """return a list of all MatchParticipant for specfic Match
               :parm request:object to pass state,WHEN page/url requested by user.
               parm pk:pass to trophyCategory id.
               """
        user_id = pk
        try:
            if user_id is not None:
                user = MatchParticipant.objects.get(id=user_id)
                serializer = MatchParticipantSerializer(user)
                return Response({"data": serializer.data})
            user = MatchParticipant.objects.all()
            serializer = MatchParticipantSerializer(user, many=True)
            return Response({"data": serializer.data})
        except:
            return Response({"message": "Unable to get MatchParticipant details with matches"})


class TrophyCategoryAPI(generics.GenericAPIView):
    serializer_class = TrophyCategorySerializer

    def post(self, request):
        """Create List of record for TrophyCategory
       :parm request:object to pass to state when request page/url requested the user
       """

        try:
            serializer = TrophyCategorySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data": serializer.data})
        except:
            return Response({"message": "Unable to create the Earned Coins"})

    def get(self, request, pk=None):
        """return a list of all TrophyCategory for specfic Trophy
        :parm request:object to pass state,WHEN page/url requested by user.
        parm pk:pass to trophyCategory id.
        """
        user_id = pk
        try:
            if user_id is not None:
                user = TrophyCategory.objects.get(id=user_id)
                serializer = TrophyCategorySerializer(user)
                return Response({"data": serializer.data})
            user = TrophyCategory.objects.all()
            serializer = TrophyCategorySerializer(user, many=True)
            return Response({"data": serializer.data})

        except:
            return Response({"message": "Unable to get the Trophy category details"})

    def put(self, request, pk=id):
        """update a list of record for trophyCategory,when request page/url requested the user
        :params pk pass the  TrophyCategory record id"""
        try:
            user_id = pk
            user = TrophyCategory.objects.get(id=user_id)
            serializer = TrophyCategorySerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg": "TrophyCategory badges is updated"})
        except:
            return Response({"message": "Unable to perform the update trophy category details"})

    def delete(self, request, pk):
        """delete a single record for trophyCategory,when request page/url requested the user
               :params pk pass the  TrophyCategory record id"""

        trophy = TrophyCategory(pk)
        trophy.delete()
        return Response({"msg": "TrophyCategory badges is deleted"})


class BadgesCategoryAPI(generics.GenericAPIView):
    serializer_class = BadgesCategorySerializer

    def post(self, request):
        """Create List of record for BadgesCategory
              :parm request:object to pass to state when request page/url requested the user
              """
        try:
            serializer = BadgesCategorySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data": serializer.data})
        except:
            return Response({"message": "Unable to create the BadgesCategory details"})

    def get(self, request, pk=None):
        """return a list of all BadgesCategory for specfic Trophy
                :parm request:object to pass state,WHEN page/url requested by user.
                parm pk:pass to BadgesCategory id.
                """
        user_id = pk
        try:
            if user_id is not None:
                user = BadgesCategory.objects.get(id=user_id)
                serializer = BadgesCategorySerializer(user)
                return Response({"data": serializer.data})
            user = BadgesCategory.objects.all()
            serializer = BadgesCategorySerializer(user, many=True)
            return Response({"data": serializer.data})
        except:
            return Response({"message": "Unable to get the BadgesCategory details"})

    def put(self, request, pk=id):
        """update a list of record for BadgesCategory,when request page/url requested the user
                :params pk pass the  BadgesCategory record id"""
        try:
            user_id = pk
            user = BadgesCategory.objects.get(id=user_id)
            serializer = BadgesCategorySerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg": "BadgesCategory badges is updated"})
        except:
            return Response({"message": "Unable to perform the update Badges category details"})

    def delete(self, request, pk):
        """delete a single record for BadgesCategory,when request page/url requested the user
                      :params pk pass the  BadgesCategory record id"""

        badges = BadgesCategory(pk)
        badges.delete()
        return Response({"msg": "BadgesCategory badges is deleted"})


class UserTrophyCaseAPI(generics.GenericAPIView):
    serializer_class = UserTrophyCaseSerializer

    def get(self, request, pk=None):
        """return a list of all BadgesCategory for specfic Trophy
                :parm request:object to pass state,WHEN page/url requested by user.
                parm pk:pass to BadgesCategory id.
                """
        user_id = pk
        try:
            if user_id is not None:
                user = UserTrophyCase.objects.get(id=user_id)
                serializer = UserTrophyCaseSerializer(user)
                return Response({"data": serializer.data})
            user = UserTrophyCase.objects.all()
            serializer = UserTrophyCaseSerializer(user, many=True)
            return Response({"data": serializer.data})
        except:
            return Response({"message": "Unable to get the UserTrophyCase details"})

    def post(self, request):
        """Create List of record for BadgesCategory
              :parm request:object to pass to state when request page/url requested the user
              """
        try:
            serializer = UserTrophyCaseSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data": serializer.data})
        except:
            return Response({"message": "Unable to create the UserTrophyCaseSerilizer details"})


class UserPlatformAPI(generics.GenericAPIView):
    serializer_class = UserPlatformSerializer

    def post(self, request):
        try:
            serializer = UserPlatformSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data": serializer.data})
        except Exception as ex:
            print(str(ex))

    def get(self, request, pk=None):
        user_id = pk
        if user_id is not None:
            user = UserPlatform.objects.get(id=user_id)
            serializer = UserPlatformSerializer(user)
            return Response({"data": serializer.data})
        user = UserPlatform.objects.all()
        serializer = UserPlatformSerializer(user, many=True)
        return Response({"data": serializer.data})


class UserGameAPI(generics.GenericAPIView):
    serializer_class = UserGameSerializer

    def post(self, request):
        try:
            serializer = UserGameSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data": serializer.data})
        except Exception as ex:
            print(str(ex))

    def get(self, request, pk=None):
        user_id = pk
        if user_id is not None:
            user = UserGame.objects.get(id=user_id)
            serializer = UserGameSerializer(user)
            return Response({"data": serializer.data})
        user = UserGame.objects.all()
        serializer = UserGameSerializer(user, many=True)
        return Response({"data": serializer.data})


class UserMatchParticipantAPI(generics.GenericAPIView):
    serializer_class = UserMatchParticipantSerializer

    def post(self, request):
        try:
            serializer = UserMatchParticipantSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data": serializer.data})
        except Exception as ex:
            print(str(ex))

    def get(self, request, pk=None):
        user_id = pk
        if user_id is not None:
            user = UserMatchParticipant.objects.get(id=user_id)
            serializer = UserMatchParticipantSerializer(user)
            return Response({"data": serializer.data})
        user = UserMatchParticipant.objects.all()
        serializer = UserMatchParticipantSerializer(user, many=True)
        return Response({"data": serializer.data})
