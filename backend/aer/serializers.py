from rest_framework import serializers
from .models import Image, Video, TextFile, Email

# Serializers for all models

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

class TextFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextFile
        fields = '__all__'

class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = '__all__'