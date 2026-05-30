from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import index, FilmViewSet, CharacterViewSet, PlanetViewSet, StarshipViewSet, seed_data

router = DefaultRouter()
router.register("films", FilmViewSet, basename="films")
router.register("characters", CharacterViewSet, basename="characters")
router.register("planets", PlanetViewSet, basename="planets")
router.register("starships", StarshipViewSet, basename="starships")

urlpatterns = [
    path("", index, name="index"),
    path("", include(router.urls)),
    path("seed/", seed_data),
]