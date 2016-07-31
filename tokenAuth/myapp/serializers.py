from rest_framework import serializers

from myapp.models import UserProfile


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ('username', 'password', 'token_field')
