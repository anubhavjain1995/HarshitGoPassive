from abc import ABC

from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import HomeCms, admin
from django.contrib.auth.hashers import make_password


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


class AdminRegistrationSerializet(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = admin
        fields = ['username', 'email', 'password', 'admin_type', 'password2', ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        account = admin(email=self.validated_data['email'],
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
    class Meta:
        model = admin
        fields = ['email','password',]

    def validate(self, attrs):
        if attrs.get('email') and attrs.get('password'):
            user = authenticate(request=self.context.get('request'),
                                email=attrs.get('email'), password=attrs.get('password'))
            if not user:
                msg = 'Unable to log in with provided credentials.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Must include "username" and "password".'
            raise serializers.ValidationError(msg, code='authorization')


        return user
        # if not attrs.get('email') == "":
        #     if not attrs.get('password') == "":
        #         account = admin.objects().get(email=attrs.get('email'), password=attrs.get('password'))
        #         return account
        #     raise serializers.ValidationError({'password': 'password doesn\'t matches'})
        # raise serializers.ValidationError({'email': 'User doesn\'t exists'})
