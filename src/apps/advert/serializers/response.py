from rest_framework import serializers


class CitySerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField()


class CategorySerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField()


class AdvertDetailSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    created = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    modified = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    title = serializers.CharField()
    description = serializers.CharField()
    city = CitySerializer()
    category = CategorySerializer()
    views = serializers.IntegerField()


class AdvertListSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    title = serializers.CharField()
    description = serializers.CharField()
    city = CitySerializer()
    category = CategorySerializer()
    views = serializers.IntegerField()
    created = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
