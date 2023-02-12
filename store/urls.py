from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('<int:customer_id>/', views.homepage, name='homepage'),
    path('create_order/', views.create_order, name='create_order'),
    path('shopping_cart/<int:customer_id>/', views.shopping_cart, name='shopping_cart'),
    path('<int:customer_id>/<int:product_id>/', views.order_form, name='order_form'),
    path('products/', views.product_list, name='product_list'),
    path('products/<int:id>/', views.product_detail, name='product_detail'),
    path('categories/', views.category_list, name='category_list'),
    path('customers/', views.customer_list, name='customer_list'),
    path('orders/', views.order_list, name='order_list'),
    path('order/<int:customer_id>/<int:product_id>/', views.order_form, name='order_form'),
    path('submit_order/<int:customer_id>/<int:product_id>/', views.submit_order, name='submit_order'),
]

