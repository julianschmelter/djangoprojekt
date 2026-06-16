from rest_framework import serializers
from .models import MeinXOEVStandard

class MeinXOEVStandardSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeinXOEVStandard
        fields = "__all__"