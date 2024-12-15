from rest_framework import serializers
from . import models
from rest_framework.exceptions import ValidationError
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator



class UserRegisterSerializer(serializers.Serializer):
    username = serializers.CharField(
        validators=[
            UniqueValidator(
                queryset=get_user_model().objects.all(),
            )
        ]
    )
    email = serializers.EmailField(
        validators=[
            UniqueValidator(
                queryset=get_user_model().objects.all(),
            )
        ]
    )
    password = serializers.CharField(
        write_only=True
    )
    confirm_password = serializers.CharField(
        write_only=True
    )
    first_name = serializers.CharField()
    last_name = serializers.CharField()


    def validate(self, attrs):
        data = super().validate(attrs)
        password = data.get('password')
        confirm_password = data.get('confirm_password')
        if password != confirm_password:
            raise ValidationError('Password mismatch')
        return data

    def create(self, validated_data):
        password = validated_data.pop('confirm_password')
        User = get_user_model()
        user = User(
            is_staff=True,
            **validated_data
        )
        user.set_password(password)
        user.save()
        return user


class UserDetailsSerializer(serializers.ModelSerializer):
    date_joined = serializers.DateTimeField(read_only=True)

    class Meta:
        model = get_user_model()
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'date_joined',
        ]


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Project
        fields = '__all__'


class ProjectDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Project
        fields = [
            'name',
            'description',
            'owner',
        ]


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Task
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = '__all__'

