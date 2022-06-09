from django.db import models

# Create your models here.

class ProductDisplay(models.Model): 
    product_id = models.PositiveIntegerField(max_length=200)
    product_title = models.CharField(max_length=200)
    image = models.CharField(max_length=500)


# for the likes 

class ProductLikes(models.Model): 
    product_id = models.PositiveIntegerField(default=500)
    likes = models.PositiveIntegerField(max_length=500)