from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass


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
