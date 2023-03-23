from django.urls import path
from  .views import *


urlpatterns = [
    path('categoryes/', CategoryCreateListView.as_view(), name="categoryes"),
    path('category/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name="category_detail"),
    path('products/', ProductCreateListView.as_view(), name="prooducts"),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name="product_detail"),
    path('brands/', BrandCreateListView.as_view(), name="brands"),
    path('brand/<int:pk>/', BrandRetrieveUpdateDestroyAPIView.as_view(), name="brand_detail"),
]