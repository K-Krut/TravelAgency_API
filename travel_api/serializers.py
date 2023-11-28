from itertools import groupby
from django.utils.translation import get_language
from rest_framework import serializers
from .models import *


class TourSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    season = serializers.StringRelatedField(many=False)

    class Meta:
        model = Tour
        fields = ('id', 'name', 'date_start', 'date_end', 'price', 'free_places', 'season', 'images')

    def get_images(self, obj):
        main_image = obj.images.filter(is_main=True).first()
        image = main_image if main_image else obj.images.filter().first()
        return image.aws_url.url if image else None

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
        fields = ('id', 'name', 'date_start', 'date_end', 'price', 'free_places', 'season', 'images')

    def get_images(self, obj):
        main_image = obj.images.filter(is_main=True).first()
        image = main_image if main_image else obj.images.filter().first()
        return image.aws_url.url if image else None

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if not representation['images']:
            representation.pop('images')
        return representation


class SiteMapSerializer(serializers.ModelSerializer):
    time_update = serializers.DateTimeField(format='%Y-%m-%dT%H:%M:%S.%fZ')

    class Meta:
        model = Tour
        fields = ('id', 'time_update')


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ('name', 'image_url')


class DetailsSerializer(serializers.ModelSerializer):
    season = serializers.StringRelatedField(many=False)
    images = serializers.SerializerMethodField()
    landmarks = serializers.SerializerMethodField()
    program = serializers.SerializerMethodField()
    options = serializers.SerializerMethodField()
    additional_options = serializers.SerializerMethodField()
    duration = serializers.SerializerMethodField()

    class Meta:
        model = Tour
        fields = ('id', 'name', 'description', 'date_start', 'date_end', 'price', 'free_places',
                  'season', 'duration', 'images', 'landmarks', 'program', 'options', 'additional_options')

    def get_images(self, obj):
        return [image.aws_url.url for image in obj.images.all()]

    def get_landmarks(self, obj):
        language = get_language()
        landmarks = obj.program.filter(is_landmark=True)[:4]
        return [
            {
                "name": landmark.tour_option.name_ru if language == 'ru' and landmark.tour_option.name_ru else landmark.tour_option.name,
                "image_url": landmark.tour_option.image_url.url
            }
            for landmark in landmarks
        ]

    def get_additional_options(self, obj):
        language = get_language()
        options = obj.adoption.all()
        return [
            {
                "name": option.name_ru if language == 'ru' and option.name_ru else option.name,
                "icon": option.icon.url if option.icon else None
            }
            for option in options
        ]

    def get_options(self, obj):
        language = get_language()
        options = obj.adoption.all()
        return [
            {
                "name": option.name_ru if language == 'ru' and option.name_ru else option.name,
                "icon": option.icon.url if option.icon else None
            }
            for option in options
        ]

    def get_program(self, obj):
        tour_programs = obj.program.all().order_by('tour_days', 'order')
        grouped_by_days = {key: list(group) for key, group in groupby(tour_programs, key=lambda p: p.tour_days.day)}
        return [{"name": day, "options": [program.tour_option.name for program in group]} for day, group in
                grouped_by_days.items()]

    def get_duration(self, obj):
        duration = obj.date_end - obj.date_start
        return duration.days
