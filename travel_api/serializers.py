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
    program = serializers.SerializerMethodField()
    options = serializers.SerializerMethodField()
    additional_options = serializers.SerializerMethodField()

    class Meta:
        model = Tour
        fields = ('id', 'name', 'date_start', 'date_end', 'price', 'free_places', 'season', 'images', 'landmarks', 'program', 'options', 'additional_options')

    def get_landmarks(self, obj):
        landmark = obj.option.filter(is_landmark=True).values('name', 'image_url')

        return landmark


    def get_additional_options(self, obj):
        additional_options = obj.adoption.filter().values('icon', 'name')

        return  additional_options

    def get_options(self, obj):
        options = obj.option.filter().values('name', 'icon')

        return options

    def get_program(self, obj):
        program = obj.program.filter().values(
            'tour_day__day',
            'tour_option__name',
            'tour_option__description',
            'tour_option__image_url',
            'tour_option__date_start',
            'tour_option__date_end',
            'tour_option__is_landmark'
        )

        return program