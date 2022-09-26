from django.shortcuts import render, redirect
from django.urls import reverse
from eshop.models import Product, Category

def product_add_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        context = {'categories': categories}
        return render(request, 'add_product.html', context=context)
    product_category = request.POST.get('category')
    category = Category.objects.get(title=product_category)
    product_data = {
        'title': request.POST.get('title'),
        'product_description': request.POST.get('product_description'),
        'category': category,
        'price': request.POST.get('price'),
        'images_url': request.POST.get('images_url')
    }
    product = Product.objects.create(**product_data)
    return redirect(reverse('product', kwargs={'pk': product.pk}))