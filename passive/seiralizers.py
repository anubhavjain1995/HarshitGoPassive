from abc import ABC

from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.response import Response

from .models import HomeCms, AdminDataTable, HomeCmsClientsSlider,UserTable,UserLeadsTable,ChangesRequestTable
from .Cryptogenerator import *


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

        # account.password = make_password(password)
        account.password = encrypt(txt=password)

        account.save()
        return account


class AdminLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)

    class Meta:
        model = AdminDataTable
        fields = ['email', 'password', 'admin_type', 'uuid', 'token']

    def validate(self, attrs):
        if not attrs.get('email') == "":
            email = AdminDataTable.objects.filter(email=attrs.get('email')).count()
            if email > 0:
                password = encrypt(txt=attrs.get('password'))
                account = AdminDataTable.objects.get(email=attrs.get('email'), password=password)
                return account

            raise serializers.ValidationError({'password': 'password doesn\'t matches'})

        raise serializers.ValidationError({'email': 'User doesn\'t exists'})


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeCmsClientsSlider
        # view all coloumns
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTable
        # view all coloumns
        fields = '__all__'


class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = UserTable
        fields='__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }


    # profile_image = self.validated_data['profile_image']
    def save(self):
        account = UserTable(email=self.validated_data['email'],
                                 username=self.validated_data['username'],
                                 user_type=self.validated_data['user_type'],
                                 contact_no=self.validated_data['contact_no'],
                                 address=self.validated_data['address']
                                 )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'password doesn\'t matches'})

        # account.password = make_password(password)
        # print(Cryptogenerator.endocedata(password))
        account.password = encrypt(txt=password)
        account.save()
        return account


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)

    class Meta:
        model = UserTable
        fields = ['email', 'password', 'user_type', 'uuid', 'token']

    def validate(self, attrs):
        if not attrs.get('email') == "":
            email = UserTable.objects.filter(email=attrs.get('email')).count()
            if email > 0:
                password = attrs.get('password')#Cryptogenerator.endocedata()
                print(password)
                account = UserTable.objects.get(email=attrs.get('email'))
                ser = UserSerializer(account)
                dp_pass = decrypt(txt=ser.data.get('password'))
                print(dp_pass)
                if password == dp_pass:
                    return account
                raise serializers.ValidationError({'password': 'password doesn\'t matches'})

            raise serializers.ValidationError({'email': 'User doesn\'t exists'})
        raise serializers.ValidationError({'email': 'Please povide a valid email'})


#leads
class UserLeadsSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserLeadsTable
        fields = '__all__'



#request form
class ChangesRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = ChangesRequestTable
        fields = '__all__'


