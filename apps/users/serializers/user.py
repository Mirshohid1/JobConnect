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

    def validate(self, data):
        new_password = data.get('new_password')
        confirm_new_password = data.get('confirm_new_password')

        if new_password or confirm_new_password:
            if not new_password:
                raise serializers.ValidationError({'new_password': 'Enter a new password.'})
            if not confirm_new_password:
                raise serializers.ValidationError({'confirm_new_password': 'Confirm the new password.'})
            if new_password != confirm_new_password:
                raise serializers.ValidationError({'confirm_new_password': "The passwords don't match."})

        return data

    def update(self, instance, validated_data):
        new_password = validated_data.pop('new_password', None)
        validated_data.pop('confirm_new_password', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if new_password:
            instance.set_password(new_password)

        instance.save()
        return instance


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
