from django.shortcuts import render, redirect
from eshop.models import Category

def category_add_view(request, *args, **kwargs):
    if request.method == 'GET':
        return render(request, 'add_category.html')
    category_data = {
        'title': request.POST.get('title'),
        'description': request.POST.get('description')
    }
    Category.objects.create(**category_data)
    return redirect('products')