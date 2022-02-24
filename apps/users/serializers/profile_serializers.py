from rest_framework import serializers

from apps.users.models import Profile


class ProfileModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'
