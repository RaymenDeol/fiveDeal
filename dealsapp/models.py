from django.db import models
from django.utils import timezone

class Item(models.Model) :
    name = models.CharField(max_length = 50)
    store_name = models.ManyToManyField('Store')
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    price = models.CharField(max_length = 50)

    def __str__(self) :
        return self.name

class Store(models.Model) :
    name = models.CharField(max_length = 50)

    def __str__(self) :
        return self.name

class Category(models.Model) :
    name = models.CharField(max_length = 50)

    def __str__(self) :
        return self.name