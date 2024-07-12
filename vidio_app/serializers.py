from rest_framework import serializers
from .models import Video

def validate_file_extension(value):
    if not value.name.endswith(('.mp4', '.avi', '.mov')):
        raise serializers.ValidationError("Fayl turi qo'llab-quvvatlanmaydi.")
    if value.size > 52428800:
        raise serializers.ValidationError("Fayl hajmi juda katta.")

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

    def validate_file(self, value):
        validate_file_extension(value)
        return value