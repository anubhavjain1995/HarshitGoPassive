from abc import ABC

from rest_framework import serializers
from .models import HomeCms,admin


class HomeSerializer(serializers.ModelSerializer):

    class Meta:
        model = HomeCms
        # view all coloumns
        fields = '__all__'

class AdminSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = admin
        # view all coloumns
        fields = '__all__'

