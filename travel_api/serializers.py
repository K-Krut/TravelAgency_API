from rest_framework import serializers
from django.forms.models import model_to_dict
from .models import *


class TourSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    season = serializers.StringRelatedField(many=False)

    class Meta:
        model = Tour
        fields = ('tour_id', 'name', 'date_start', 'date_end', 'price', 'free_places', 'season', 'images')

    def get_images(self, obj):
        main_image = obj.images.filter(is_main=True).first()
        return main_image.aws_url if main_image else None

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if not representation['images']:
            representation.pop('images')
        return representation


class FeaturedSerializer(serializers.ModelSerializer):
    season = serializers.StringRelatedField(many=False)
    images = serializers.SerializerMethodField()

    class Meta:
        model = Tour
        fields = ('tour_id', 'name', 'date_start', 'date_end', 'price', 'free_places', 'season', 'images')

    def get_images(self, obj):
        main_image = obj.images.filter(is_main=True).first()
        return main_image.aws_url if main_image else None

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if not representation['images']:
            representation.pop('images')
        return representation



class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ('name', 'image_url')


class DetailsSerializer(serializers.ModelSerializer):
    season = serializers.StringRelatedField(many=False)
    images = serializers.StringRelatedField(many=True)
    landmarks = serializers.SerializerMethodField()

    class Meta:
        model = Tour
        fields = ('id', 'name', 'date_start', 'date_end', 'price', 'free_places', 'season', 'images', 'landmarks')

    def get_landmarks(self, obj):
        landmark = obj.option.filter(is_landmark=True).values()

        return landmark