from rest_framework import serializers
from .models import *

class categoryserializer(serializers.ModelSerializer):
    class Meta:
        model=category
        fields ='__all__'