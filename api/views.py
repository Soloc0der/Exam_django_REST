from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from main.serializers import *
from main.models import *



class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = "pk"

class CategoryCreateListView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        queryset = Category.objects.all()
        name = self.request.query_params.get("name")
        if name is not None:
            return Category.objects.filter(title__icontains=name) 
        return queryset



class ProductCreateListView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        name = self.request.query_params.get("name")
        if name is not None:
            return Product.objects.filter(title__icontains=name) 
        return queryset

class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"



class BrandRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    lookup_field = "pk"
    




class BrandCreateListView(ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

    def get_queryset(self):
        queryset = Brand.objects.all()
        name = self.request.query_params.get("name")
        if name is not None:
            return Brand.objects.filter(title__icontains=name) 
        return queryset
