from rest_framework import serializers

from .models import Build

class BuildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Build
        fields = ('id', 'code', 'offerings',)
