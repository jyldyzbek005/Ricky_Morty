from dataclasses import field
from rest_framework import serializers
from .models import CustomUser

class CustomerUserSerializers(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'})


    class Meta:
        model = CustomUser
        field = ('id', 'last_name', 'first_name', 'middle_name', 'user_name', 'email', 'password')

        extra_kwargs = {
            'id': {'read_only': True},
            'password': {'write_only': True}

        }

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            last_name=validated_data['lastname'],
            first_name=validated_data['firstname'],
            middle_name=validated_data['middlename'],
            email=validated_data['email'] )
        user.set_password(validated_data['password'])
        user.save()
        return user