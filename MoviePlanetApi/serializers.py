from rest_framework import serializers
from .models import Planet, Character, Film, Starship


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = "__all__"


class FilmSerializer(serializers.ModelSerializer):
    characters = CharacterSerializer(many=True, read_only=True)
    characters_id = serializers.PrimaryKeyRelatedField(
        queryset=Character.objects.all(),
        source="characters",
        write_only=True,
        many=True
    )

    class Meta:
        model = Film
        fields = "__all__"


class PlanetSerializer(serializers.ModelSerializer):
    residents = CharacterSerializer(many=True, read_only=True)
    residents_id = serializers.PrimaryKeyRelatedField(
        queryset=Character.objects.all(),
        source="residents",
        write_only=True,
        many=True
    )

    class Meta:
        model = Planet
        fields = "__all__"


class StarshipSerializer(serializers.ModelSerializer):
    pilots = CharacterSerializer(many=True, read_only=True)
    pilots_id = serializers.PrimaryKeyRelatedField(
        queryset=Character.objects.all(),
        source="pilots",
        write_only=True,
        many=True
    )

    class Meta:
        model = Starship
        fields = "__all__"