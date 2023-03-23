from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self) -> str:
        return self.title


class Brand(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.title



class Product(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="photo/")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="product")
    brand_id = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="brand")

    def __str__(self) -> str:
        return self.title


