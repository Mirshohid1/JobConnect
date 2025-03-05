from rest_framework import serializers

from .skill import SkillSerializer

from users.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'role')


class UserInputSerializer(serializers.ModelSerializer):
    new_password = serializers.CharField()
    confirm_new_password = serializers.CharField()

    pass


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
