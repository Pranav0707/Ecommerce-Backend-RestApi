import imp
from django.urls import path,include
from .views import CategoryDetail, ProductDetail, ProductsList,create_category,create_product

urlpatterns=[
    path('products_list/',ProductsList.as_view()),
    path('products_detail/<slug:category_slug>/<slug:product_slug>/',ProductDetail.as_view()),
    path('category_detail/<slug:category_slug>/',CategoryDetail.as_view()),
    path('create_category/',create_category),
    path('create_product/',create_product)
]