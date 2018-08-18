from django.http import HttpResponse
from django.shortcuts import render

def home_view(request):
    return render(request, "pages/home.html",{})


def contact_view(request):
    return render(request, "pages/contact.html",{})


def about_view(request):
    my_context= {
        "my_text": "This is about view",
        "my_number": 123,
        "num_list": [123,345,456]
    }
    return render(request, "pages/about.html", my_context)

# def social_view(request):
#     return render(request, "product/home.html",{})
