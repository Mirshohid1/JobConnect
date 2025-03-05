from rest_framework import serializers

from .skill import SkillSerializer


class UserSerializer(serializers.ModelSerializer):
    pass


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
