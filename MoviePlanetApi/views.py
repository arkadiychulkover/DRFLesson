from rest_framework import viewsets
from django.shortcuts import render
from django.http import JsonResponse
from .models import Film, Character, Planet, Starship
from .serializers import FilmSerializer, CharacterSerializer, PlanetSerializer, StarshipSerializer

def index(request):
    return render(request, "index.html")

def seed_data(request):
    Character.objects.all().delete()
    Film.objects.all().delete()
    Planet.objects.all().delete()
    Starship.objects.all().delete()

    luke = Character.objects.create(name="Luke Skywalker", species="Human", gender="Male", age=19)
    vader = Character.objects.create(name="Darth Vader", species="Human", gender="Male", age=45)

    film1 = Film.objects.create(
        title="A New Hope",
        episode=4,
        description="First Star Wars movie",
        release_date="1977-05-25"
    )

    film2 = Film.objects.create(
        title="The Empire Strikes Back",
        episode=5,
        description="Dark continuation",
        release_date="1980-05-21"
    )

    film1.characters.add(luke, vader)
    film2.characters.add(vader)

    tatooine = Planet.objects.create(
        name="Tatooine",
        climate="Hot",
        terrain="Desert",
        population=200000
    )

    tatooine.residents.add(luke)

    falcon = Starship.objects.create(
        name="Millennium Falcon",
        model="YT-1300",
        manufacturer="Corellian Engineering",
        cost=100000,
        crew=4
    )

    falcon.pilots.add(luke)

    return JsonResponse({"message": "Database seeded successfully"})

class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

class PlanetViewSet(viewsets.ModelViewSet):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer

class StarshipViewSet(viewsets.ModelViewSet):
    queryset = Starship.objects.all()
    serializer_class = StarshipSerializer