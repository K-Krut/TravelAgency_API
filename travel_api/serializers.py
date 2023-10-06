from rest_framework import serializers
from .models import *


class TourSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    season = serializers.StringRelatedField(many=True)

    class Meta:
        model = Tour
        fields = ('id', 'name', 'date_start', 'date_end', 'price', 'free_places', 'season', 'images')

    # TODO нужно возвращать первую существующую картинку, если нет картинки с индикатором ис меин,
    #  а если картинок вообще нет, то не возвращать поле имеджис (я уже это сделала)

    def get_images(self, obj):
        main_image = obj.images.filter(is_main=True).first()
        return main_image.aws_url if main_image else None

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if not representation['images']:
            representation.pop('images')
        return representation
