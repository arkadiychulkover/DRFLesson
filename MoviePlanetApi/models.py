import uuid
from django.db import models


class Film(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    episode = models.IntegerField()
    description = models.TextField(blank=True)
    release_date = models.DateField()

    def __str__(self):
        return self.title


class Character(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    species = models.CharField(max_length=255, blank=True)
    gender = models.CharField(max_length=50, blank=True)
    age = models.IntegerField(null=True, blank=True)

    films = models.ManyToManyField(Film, related_name="characters", blank=True)

    def __str__(self):
        return self.name


class Planet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)
    climate = models.CharField(max_length=255, blank=True)
    terrain = models.CharField(max_length=255, blank=True)
    population = models.BigIntegerField(null=True, blank=True)

    residents = models.ManyToManyField(Character, related_name="planets", blank=True)

    def __str__(self):
        return self.name


class Starship(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=255, blank=True)
    manufacturer = models.CharField(max_length=255, blank=True)
    cost = models.BigIntegerField(null=True, blank=True)
    crew = models.IntegerField(null=True, blank=True)

    pilots = models.ManyToManyField(Character, related_name="starships", blank=True)

    def __str__(self):
        return self.name