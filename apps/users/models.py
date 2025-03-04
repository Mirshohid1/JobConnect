from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser


def path_to_avatar(instance, filename):
    return f"media/user_{instance.id}/avatar-{filename}"


class CustomUser(AbstractUser):
    CHOICES_ROLE = [
        ('user', 'User'),
        ('admin', 'Admin')
    ]

    email = models.EmailField(_("email address"), unique=True, null=True, blank=True)
    avatar = models.ImageField(upload_to=path_to_avatar, null=True, blank=True, verbose_name=_("Avatar"))
    bio = models.TextField(null=True, blank=True, verbose_name=_("Bio"))
    role = models.CharField(max_length=10, choices=CHOICES_ROLE, default='user')
    birth_date = models.DateField(null=True, blank=True)
    is_email_verified = models.BooleanField(default=False)


class SkillType(models.Model):
    pass


class Skill(models.Model):
    pass


class ProfessionType(models.Model):
    pass


class Profession(models.Model):
    pass


class UserSkill(models.Model):
    pass


class UserProfession(models.Model):
    pass
