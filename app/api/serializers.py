from rest_framework import serializers
from .models import Game, User, Subscription
from rest_framework.fields import CurrentUserDefault

class GameSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=256)
    publisher_id = CurrentUserDefault()

    def create(self, validated_data):
        return Game.objects.create(**validated_data)

class GameGetSerializer(serializers.ModelSerializer):
    class Meta:
         model = Game
         fields = ['id', 'title','publisher_id', 'created_date']
