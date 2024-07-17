from django.urls import path

from apps.cart.views import CreateCartView, ListCartView, ListCartViewJson, UpdateCartView, DeleteCartView

urlpatterns = [
    path('admin/cart/add', CreateCartView.as_view(), name='admin-cart-add'),
    path('admin/cart/list', ListCartView.as_view(), name='admin-cart-list'),
    path('admin/cart/list/ajax', ListCartViewJson.as_view(), name='admin-cart-list-ajax'),
    path('admin/cart/edit/<int:pk>', UpdateCartView.as_view(), name='admin-cart-edit'),
    path('admin/cart/delete/<int:pk>', DeleteCartView.as_view(), name='admin-cart-delete'),
]