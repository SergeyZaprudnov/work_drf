import re

from rest_framework import serializers


def validate_content(value):
    pattern = r'(https?://)?(www\.)?youtube\.com'
    if not re.search(pattern, value):
        raise serializers.ValidationError("Содержатся недопустимые ссылки.")
    return value
