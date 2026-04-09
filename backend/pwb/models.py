from django.db import models
from django.utils import choices


class PWBUnit(models.Model):
    unit_name = models.CharField(max_length=100)

    def __str__(self):
        return self.unit_name


class Skill(models.Model):
    name = models.CharField(max_length=100)
    pwb_unit = models.ForeignKey(
        PWBUnit, on_delete=models.CASCADE, related_name="skills"
    )

    def __str__(self):
        return self.name


class Link(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    pwb_unit = models.ForeignKey(
        PWBUnit, on_delete=models.CASCADE, related_name="links"
    )

    def __str__(self):
        return self.name


class Language(models.Model):
    class Level(models.TextChoices):
        A1_Begginer = "A1 Begginer", "A1 Begginer"
        A2_Elementary = "A2 Elementary", "A2 Elementary"
        B1_Intermediate = "B1 Intermediate", "B1 Intermediate"
        B2_Upper_Intermediate = "B2 Upper-Intermediate", "B2 Upper-Intermediate"
        C1_Advanced = "C1 Advanced", "C1 Advanced"
        C2_Advanced_Proficy = "C2 Advanced Proficy", "C2 Advanced Proficy"
        Native_or_Bilingual = "Native or Bilingual", "Native or Bilingual"

    name = models.CharField(max_length=100)
    level = models.CharField(choices=Level.choices)
    pwb_unit = models.ForeignKey(
        PWBUnit, on_delete=models.CASCADE, related_name="languages"
    )

    def __str__(self):
        return self.name


# class ExperienceUnit(models.Model):
#     pass
#
#
# class Project(models.Model):
#     pass
#
#
# class EducationUnit(models.Model):
#     pass
#
#
# class Photo(models.Model):
#     pass
