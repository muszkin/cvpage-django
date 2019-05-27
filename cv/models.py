from django.db import models

# Create your models here.


class Skill(models.Model):
    name = models.CharField(max_length=255)
    value = models.IntegerField()


class Shool(models.Model):
    name = models.CharField(max_length=255)
    startDate = models.DateField()
    endDate = models.DateField()
    endTitle = models.CharField(max_length=255)


class Work(models.Model):
    company = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    startDate = models.DateField()
    endDate = models.DateField()


class Duty(models.Model):
    description = models.CharField(max_length=255)
    work = models.ForeignKey(Work, related_name="duties", on_delete=models.CASCADE)


class Testimonial(models.Model):
    name = models.CharField(max_length=255)
    project = models.CharField(max_length=255)
    projectUrl = models.CharField(max_length=255)
    testimonial = models.TextField()