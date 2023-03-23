from .models import *
from rest_framework import serializers


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ("title",)
        read_only_fields = ("id" ,)



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("title", "slug")
        read_only_fields = ("id" ,)

class ProductSerializer(serializers.ModelSerializer):
    cat = serializers.SerializerMethodField()



    class Meta:
        model = Product
        fields = ("title", "desc", "image", "price", "category", "brand_id", "cat") # "__all__"
        read_only_fields = ('id',)

    def get_cat(self, obj):
        return obj.category.title
    






