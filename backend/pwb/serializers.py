from django.forms import fields
from rest_framework import serializers

from .models import (EducationUnit, ExperienceUnit, Language, Link, PWBUnit,
                     Skill, Photo)

class PhotoSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    
    class Meta:
        model = Photo
        fields = ["image", "is_main"]

    def get_image(self, obj):
        if obj.image:
            return obj.image.url
        return None

class EducationUnitSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    class Meta:
        model = EducationUnit
        fields = ["name", "description", "from_date", "to_date", "image"]

    def get_image(self, obj):
        if obj.image:
            return obj.image.url
        return None

class ExperienceUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperienceUnit
        fields = ["name", "description", "from_date", "to_date"]


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ["name"]


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ["name", "url"]


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ["name", "level"]


class PWBUnitSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True)
    links = LinkSerializer(many=True)
    languages = LanguageSerializer(many=True)
    experience_units = ExperienceUnitSerializer(many=True)
    education_units = EducationUnitSerializer(many=True)
    photos = PhotoSerializer(many=True)

    class Meta:
        model = PWBUnit
        fields = [
            "frist_name",
            "last_name",
            "email",
            "about",
            "skills",
            "links",
            "languages",
            "experience_units",
            "education_units",
            "photos"
        ]
