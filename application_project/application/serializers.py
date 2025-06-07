from rest_framework import serializers
from .models import Application
import re

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'

    def validate_name(self, value):
        if not value.istitle():
            raise serializers.ValidationError("Имя должно начинаться с заглавной буквы.")
        if not re.match(r'^[А-Яа-яA-Za-z]+$', value):
            raise serializers.ValidationError("Имя должно содержать только буквы.")
        return value

    def validate_phone(self, value):
        if not value.isdigit() and not value.startswith('+'):
            raise serializers.ValidationError("Телефон должен содержать только цифры или начинаться с '+'.")
        if len(value) < 10 or len(value) > 15:
            raise serializers.ValidationError("Телефон должен быть от 10 до 15 символов.")
        return value
