from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from users.models import Profession, ProfessionType, Skill
from .skill import SkillSerializer


class ProfessionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessionType
        fields = ('id', 'name', 'description')


class ProfessionTypeInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessionType
        fields = ('name', 'description')


class ProfessionSerializer(serializers.ModelSerializer):
    profession_type = ProfessionTypeSerializer(read_only=True)
    required_skills = SkillSerializer(many=True, read_only=True)

    class Meta:
        model = Profession
        fields = ('id', 'name', 'description', 'profession_type', 'required_skills')


class ProfessionInputSerializer(serializers.ModelSerializer):
    profession_type = PrimaryKeyRelatedField(
        queryset=ProfessionType.objects.all()
    )
    required_skills = PrimaryKeyRelatedField(
        queryset=Skill.objects.all(), many=True
    )

    class Meta:
        model = Profession
        fields = ('name', 'description', 'profession_type', 'required_skills')
