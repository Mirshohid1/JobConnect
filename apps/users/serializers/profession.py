from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from users.models import Profession, ProfessionType, Skill
from .skill import SkillSerializer


class ProfessionTypeSerializer(serializers.ModelSerializer):
    pass


class ProfessionTypeInputSerializer(serializers.ModelSerializer):
    pass


class ProfessionSerializer(serializers.ModelSerializer):
    profession_type = ProfessionTypeSerializer(read_only=True)
    required_skills = SkillSerializer(many=True, read_only=True)

    pass


class ProfessionInputSerializer(serializers.ModelSerializer):
    profession_type = PrimaryKeyRelatedField(
        queryset=ProfessionType.objects.all()
    )
    required_skills = PrimaryKeyRelatedField(
        queryset=Skill.objects.all(), many=True
    )

    pass
