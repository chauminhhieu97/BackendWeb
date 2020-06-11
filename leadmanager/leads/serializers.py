from rest_framework import serializers
# from leads.models import Lead, user, movie
from leads.models import Lead, User, movie, tag, link, rating
from django.contrib.auth import authenticate

# Lead Serializer


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = movie
        fields = '__all__'

# Test


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = tag
        fields = '__all__'


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = link
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = rating
        fields = '__all__'


# Manh
# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'is_staff')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):

        user = User.objects.create_user(
            validated_data['username'], validated_data['email'], validated_data['password'])
        print(validated_data)
        return user

# Login Serializer


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):

        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.gender = validated_data.get('gender', instance.gender)

        return instance
