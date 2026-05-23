from rest_framework import serializers
from .models import Product, Project, Task

class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductSerializer(serializers.Serializer):
    productId = serializers.UUIDField(read_only=True)
    name = serializers.CharField(max_length=100)
    description = serializers.CharField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)

    def get_full_info(self, obj: Product):
        return f"{obj.name} - {obj.description} - ${obj.price}"

    def get_price_usd(self, obj: Product):
        rate = self.context.get('usd_rate', 43)
        return round(obj.price / rate, 2)

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be less than zero.")
        return value

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance
    


class ProjectModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class TaskModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'