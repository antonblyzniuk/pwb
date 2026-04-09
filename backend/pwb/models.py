from django.db import models


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

# class Link(models.Model):
#     pass
# 
# 
# class Language(models.Model):
#     pass
# 
# 
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
