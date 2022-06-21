from abc import ABC

from rest_framework import serializers
from .models import HomeCms


class HomeSerializer(serializers.ModelSerializer):

    class Meta:
        model = HomeCms
        # view all coloumns
        fields = '__all__'

