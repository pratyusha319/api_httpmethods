from app.models import *
from rest_framework import serializers

class Product_c_s(serializers.ModelSerializer):
    class Meta:
        model=Product_category
        fields='__all__'
class Product_s(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'      