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
    skill_type = serializers.PrimaryKeyRelatedField(
        queryset=SkillType.objects.all()
    )

    class Meta:
        model = Skill
        fields = ('name', 'description', 'skill_type')

    def to_internal_value(self, data):
        skill_type_data = data.get('skill_type')

        if isinstance(skill_type_data, dict):
            try:
                skill_type = SkillType.objects.get(**skill_type_data)
            except SkillType.DoesNotExist:
                raise serializers.ValidationError(
                    {"skill_type": "Skill type not found, provide a valid ID."}
                )
            data['skill_type'] = skill_type.id

        return super().to_internal_value(data)
