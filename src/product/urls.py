from django.contrib import admin
from django.urls import path

from . import views

app_name="product"

urlpatterns = [
    path('<int:my_id>/', views.product_detail_view,name="product_detail" ),
    path('create/', views.product_create_view,name="product_create_view" ),
    path('<int:my_id>/delete/', views.product_delete_view,name="product_delete_view" ),
    path('list/', views.product_list_view,name="product_list_view" ),
]
