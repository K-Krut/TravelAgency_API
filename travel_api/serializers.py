from rest_framework import serializers
from .models import *


class TourSerializer(serializers.ModelSerializer):
    images = serializers.StringRelatedField(many=True)
    season = serializers.StringRelatedField(many=True)

    class Meta:
        model = Tour
        # fields = ('id', 'tour_image')
        fields = ('id', 'name', 'date_start', 'date_end', 'price', 'free_places', 'season', 'images')
