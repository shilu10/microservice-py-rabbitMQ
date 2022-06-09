from rest_framework import serializers
from .models import *

class ProductDisplaySerializer(serializers.ModelSerializer): 
    class Meta: 
        model = ProductDisplay
        fields = "__all__"

class ProductLikesSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = ProductLikes
        fields = "__all__"
