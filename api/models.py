from django.db import models


class Project(models.Model):
    name: models.CharField(max_length=30)
    description: models.CharField(max_length=150)
    created: models.DateField()
    statut: models.BooleanField
    link: models.CharField(max_length=200)
    picture: models.CharField(max_length=255)
    created_ad: models.DateTimeField
