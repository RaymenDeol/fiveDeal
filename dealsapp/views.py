from django.shortcuts import render
from .models import Item

def category_list(request) :

    items = Item.objects.all()
    item_prices = Item.objects.all().values('price')
    store_names = Item.objects.all().values('store_name')
    categories = Item.objects.all().values('category')


    return render(request, 'dealsapp/category_list.html', {'items': items, "item_prices": item_prices, "store_names": store_names, "categories": categories})