from django.shortcuts import render, get_object_or_404
from eshop.models import Category


def categories_view(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'categories.html', context=context)

def delete_category_view(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'categories.html', context=context)

def category_edit_view(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "GET":
        context = {
            'category': category
        }
        return render(request, 'edit_category.html', context=context)
    category.title = request.POST.get('title')
    category.description = request.POST.get('description')
    category.save()
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'categories.html', context=context)
