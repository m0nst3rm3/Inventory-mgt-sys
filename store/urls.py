from django.urls import path

from .views import (
    create_supplier,
    create_buyer,
    create_product,
    create_order,
    SupplierListView,
    BuyerListView,
    ProductListView,
    OrderListView,
)

urlpatterns = [
    path('create-supplier/', create_supplier, name='create-supplier'),
    path('create-buyer/', create_buyer, name='create-buyer'),
    path('create-product/', create_product, name='create-product'),
    path('create-order/', create_order, name='create-order'),

    path('supplier-list/', SupplierListView.as_view(), name='supplier-list'),
    path('buyer-list/', BuyerListView.as_view(), name='buyer-list'),
    path('product-list/', ProductListView.as_view(), name='product-list'),
    path('order-list/', OrderListView.as_view(), name='order-list'),
]
