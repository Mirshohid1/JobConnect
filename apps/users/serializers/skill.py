from rest_framework import serializers

from users.models import SkillType, Skill


class SkillTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillType
        fields = ('id', 'name', 'description')


class SkillTypeInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillType
        fields = ('name', 'description')


class SkillSerializer(serializers.ModelSerializer):
    skill_type = SkillTypeSerializer(read_only=True)

    class Meta:
        model = Skill
        fields = ('id', 'name', 'description', 'skill_type')


class SkillInputSerializer(serializers.ModelSerializer):
    pass
