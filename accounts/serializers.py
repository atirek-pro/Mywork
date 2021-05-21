from rest_framework import serializers
from django.contrib.auth.models import User

class UserRegisterSerializer(serializers.ModelSerializer):
    password1 =serializers.CharField(required=True, write_only=True)
    password2 =serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
        ]

        extra_kwargs = {
            'password1': {'write_only': True},
            'password2': {'write_only': True},
        }

    def create(self, validated_data):
        username = validated_data.get('username')
        email = validated_data.get('email')
        password1 = validated_data.get('password1')
        password2 = validated_data.get('password2')

        if password1 == password2:
            user = User(username=username, email=email)
            user.set_password(password1)
            user.save()
            return user
        else:
            raise serializers.ValidationError({
                'error': 'Passwords do not match'
            })



