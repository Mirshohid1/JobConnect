from rest_framework import serializers

from users.models import SkillType, Skill


class SkillTypeSerializer(serializers.ModelSerializer):
    pass


class SkillTypeInputSerializer(serializers.ModelSerializer):
    pass


class SkillSerializer(serializers.ModelSerializer):
    skill_type = SkillTypeSerializer(read_only=True)
    pass


class SkillInputSerializer(serializers.ModelSerializer):
    pass
