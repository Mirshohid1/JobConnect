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

    def to_internal_value(self, data):
        profession_type_data = data.get('profession_type')
        required_skills_data = data.get('required_skills', [])

        if required_skills_data and isinstance(required_skills_data, list):
            skill_ids = []
            for skill in required_skills_data:
                if isinstance(skill, dict):  # Nested object
                    try:
                        skill_obj = Skill.objects.get(**skill)
                    except Skill.DoesNotExist:
                        raise serializers.ValidationError(
                            {"required_skills": "Some skills were not found, provide valid IDs."}
                        )
                    skill_ids.append(skill_obj.id)
                else:  # ID (the usual case)
                    skill_ids.append(skill)

            data['required_skills'] = skill_ids

        if isinstance(profession_type_data, dict):
            try:
                profession_type = ProfessionType.objects.get(**profession_type_data)
            except ProfessionType.DoesNotExist:
                raise serializers.ValidationError(
                    {"profession_type": "Profession type not found, provide a valid ID."}
                )
            data['profession_type'] = profession_type.id

        return super().to_internal_value(data)
