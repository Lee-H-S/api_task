from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the users object"""

    class Meta:
        model = get_user_model()
        fields = ("email", "display_name", "password", "account_type")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        """Create a new user with encrypted password and return it"""
        return get_user_model().objects.create_user(**validated_data)


class AuthTokenSerializer(serializers.Serializer):
    """Serializer for the user authentication object"""

    email = serializers.CharField()
    password = serializers.CharField(
        style={"input_type": "password"}, trim_whitespace=False
    )

    def validate(self, attributes):
        """"Validate the User"""
        email = attributes.get("email")
        password = attributes.get("password")
        display_name = attributes.get("display_name")

        user = authenticate(
            request=self.context.get("request"),
            username=email,
            display_name=display_name,
            password=password,
        )

        if not user:
            message = "Unable to authenticate"
            raise serializers.ValidationError(message, code="authentication")

        attributes["user"] = user
        return attributes
