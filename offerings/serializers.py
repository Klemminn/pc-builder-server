from rest_framework import serializers

from .models import Offering

class OfferingSerializer(serializers.ModelSerializer):
    retailer_name = serializers.ReadOnlyField(source='retailer.name')
    retailer_code = serializers.ReadOnlyField(source='retailer.code')
    class Meta:
        model = Offering
        fields = ('id', 'retailer_name', 'retailer_code', 'price', 'url',)
