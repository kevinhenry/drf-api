from rest_framework import serializers
from .models import Plog

class PlogSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'author', 'header', 'note', 'created_at', 'update_at')
        model = Plog