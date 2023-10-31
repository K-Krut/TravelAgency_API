from itertools import groupby

from rest_framework import serializers
from django.forms.models import model_to_dict
from django.db.models import F, ExpressionWrapper, fields, Count
from .models import *
import datetime


def check_none(obj):
    return None if obj is None else obj.aws_url


class TourSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    season = serializers.StringRelatedField(many=False)

    class Meta:
        model = Tour
        fields = ('id', 'name', 'date_start', 'date_end', 'price', 'free_places', 'season', 'images')

    def get_images(self, obj):
        main_image = obj.images.filter(is_main=True).first()

        return main_image.aws_url if main_image else check_none(obj.images.filter().first())

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
    images = serializers.SerializerMethodField()
    landmarks = serializers.SerializerMethodField()
    program = serializers.SerializerMethodField()
    options = serializers.SerializerMethodField()
    additional_options = serializers.SerializerMethodField()
    duration = serializers.SerializerMethodField()

    class Meta:
        model = Tour
        fields = ('id', 'name', 'date_start', 'date_end', 'price', 'free_places', 'season', 'duration', 'images',
                  'landmarks', 'program', 'options', 'additional_options')

    def get_images(self, obj):
        return [image.aws_url for image in obj.images.all()]

    def get_landmarks(self, obj):
        # return obj.program.filter(is_landmark=True).values('tour_option__name', 'image_url')[:4]
        return obj.program.filter(is_landmark=True).annotate(name=F('tour_option__name')).values('name',
                                                                                                 'image_url')[:4]

    def get_additional_options(self, obj):
        return obj.adoption.filter().values('icon', 'name')

    def get_options(self, obj):
        return obj.option.filter().values('name', 'icon')

    def get_program(self, obj):
        tour_programs = obj.program.all().order_by('tour_days', 'order')
        grouped_by_days = {key: list(group) for key, group in groupby(tour_programs, key=lambda p: p.tour_days.day)}
        return [{"name": day, "options": [program.tour_option.name for program in group]} for day, group in
                grouped_by_days.items()]

    def get_duration(self, obj):
        duration = obj.date_end - obj.date_start
        return duration.days
