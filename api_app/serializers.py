from rest_framework import serializers
from .models import Text


class TextSerializer(serializers.Serializer):
    input_text = serializers.CharField()
    summary = serializers.CharField(required=False)
    bullets = serializers.ListField(child=serializers.CharField(),required=False,default=list)

    def create(self,validated_data):
        return Text.objects.create(**validated_data)
