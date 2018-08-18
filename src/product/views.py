from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect

from .models import Product
from .forms import ProductForm, RawProductForm

# def product_create_view(request):

#     form = RawProductForm()
#     if request.method == "POST":
#         form = RawProductForm(request.POST)
        
#         if form.is_valid():
#             print(form.cleaned_data)
#             Product.objects.create(**form.cleaned_data)
#         else:
#             print(form.erros)
#         form = RawProductForm()
#     context = {
#         'form': form
#     }
#     return render(request, 'product/create.html', context)

def product_create_view(request):
    print(request.POST) # <QueryDict: {'csrfmiddlewaretoken': ['srWG1u7j0pLtnmDHkcMhnZyX7B2XC5WLiuf7pDd26UjTtlWE57wbmCnvoBeIGf6j'], 'title': ['권태형'], 'description': ['테스트'], 'price': ['10.22']}>
    form = ProductForm(request.POST or None)
    print(form) # form html 코드

    if form.is_valid(): 
        form.save() #데이터베이스에 저장
        form = ProductForm() # 화면에 보일 form을 빈것으로 저장한다.
    context = {
        'form': form
    }

    return render(request, 'product/create.html', context)

# def product_detail_view(request, my_id):
#     obj = Product.objects.get(id=my_id)
#     return render(request,'product/detail.html',{'object': obj})

def product_detail_view(request, my_id):
    
    #obj = get_object_or_404(Product, id=my_id)
    
    try:
        obj = Product.objects.get(id=my_id)
    except Product.DoesNotExist:
        raise Http404
    return render(request,'product/detail.html',{'object': obj})



def product_delete_view(request, my_id):
    
    obj = get_object_or_404(Product, id=my_id)

    if request.method == 'POST':        
        obj.delete()
        return redirect('../../../home')

    return render(request,'product/delete.html',{'object': obj})


def product_list_view(request):
    obj = Product.objects.all()
    context = {
        'object_list': obj
    }
    return render(request, 'product/list.html', context)
