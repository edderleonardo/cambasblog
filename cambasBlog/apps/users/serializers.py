from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from rest_framework import serializers
from ..core.models import Country
from ..core.serializers import CountrySerializer

User = get_user_model()


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        user = authenticate(**attrs)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'email')


class RegisterUserSerializer(serializers.ModelSerializer):
    country = serializers.PrimaryKeyRelatedField(
        queryset=Country.objects.all())

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'name',
            'last_name',
            'country']
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        """Create a new user with encrypted password and return it"""
        user = User.objects.create_user(**validated_data)
        return user


class AuthorSerializer(serializers.ModelSerializer):
    country = CountrySerializer()

    class Meta:
        model = User
        fields = [
            'id',
            'name',
            'last_name',
            'email',
            'country']
