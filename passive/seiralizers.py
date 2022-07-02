from abc import ABC

from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.response import Response

from .models import HomeCms, AdminDataTable
from django.contrib.auth.hashers import make_password, check_password


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeCms
        # view all coloumns
        fields = '__all__'


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminDataTable
        # view all coloumns
        fields = '__all__'


class AdminRegistrationSerializet(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = AdminDataTable
        fields = ['username', 'email', 'password', 'admin_type', 'password2', ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        account = AdminDataTable(email=self.validated_data['email'],
                                 username=self.validated_data['username'],
                                 admin_type=self.validated_data['admin_type'],
                                 )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'password doesn\'t matches'})

        account.password = make_password(password)

        account.save()
        return account


class AdminLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)

    class Meta:
        model = AdminDataTable
        fields = ['email', 'password']

    def validate(self, attrs):
        if not attrs.get('email') == "":
            email = AdminDataTable.objects.filter(email=attrs.get('email')).count()
            if email > 0:
                account = AdminDataTable.objects.get(email=attrs.get('email'), password=attrs.get('password'))
                return account

            raise serializers.ValidationError({'password': 'password doesn\'t matches'})

        raise serializers.ValidationError({'email': 'User doesn\'t exists'})
