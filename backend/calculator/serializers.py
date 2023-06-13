import os
from rest_framework import serializers
from django.conf import settings
from .models import CalculatorTask, CalculatorResult


class CalculatorResultSerializer(serializers.ModelSerializer):

    class Meta:
        model = CalculatorResult
        fields = ['column', 'result']
        read_only_fields = ['column', 'result']


class CalculatorTaskSerializer(serializers.ModelSerializer):
    filename = serializers.RegexField(
        '^[A-zА-я0-9\.\-\ ]+\.csv$',
        max_length=255
    )
    status = serializers.IntegerField(read_only=True)
    results = CalculatorResultSerializer(many=True, read_only=True)

    class Meta:
        model = CalculatorTask
        fields = ['id', 'status', 'filename', 'results']

    def validate_filename(self, value):
        if not os.path.exists(os.path.join(settings.CSV_FILES_PATH, value)):
            raise serializers.ValidationError('Файл не найден')
        return value
