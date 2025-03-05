from rest_framework import serializers

from .skill import SkillSerializer

from users.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            'id', 'avatar',
            'first_name', 'last_name', 'username',
            'bio', 'birth_date',
            'skills', 'profession',
            'email', 'new_password', 'confirm_new_password',
        )


class UserInputSerializer(serializers.ModelSerializer):
    new_password = serializers.CharField()
    confirm_new_password = serializers.CharField()

    class Meta:
        model = CustomUser
        fields = (
            'avatar',
            'first_name', 'last_name', 'username',
            'bio', 'birth_date',
            'skills', 'profession',
            'email', 'new_password', 'confirm_new_password',
        )


class UserSkillSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    skill = SkillSerializer()

    pass


class UserSKillInputSerializer(serializers.ModelSerializer):
    pass


class UserProfessionSerializer(serializers.ModelSerializer):
    pass


class UserProfessionInputSerializer(serializers.ModelSerializer):
    pass
