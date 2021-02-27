from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Game, Subscription
from .serializers import GameSerializer, GameGetSerializer
from django.contrib.auth.decorators import login_required


class GameView(APIView):
    """
    API View for the Game Model
    """

    def get(self, request):
        """
        Method for returning serialized Game objects
        """
        games = Game.objects.all()
        serializer = GameGetSerializer(games, many=True)
        return Response({"games": serializer.data})

    @login_required
    def post(self, request):
        game = request.data.get("game")
        serializer = GameSerializer(data=game)
        if serializer.is_valid(raise_exception=True):
            game_saved = serializer.save()
        return Response(
            {"success": "Game: '{}' successfully created.".format(game_saved.title)}
        )
