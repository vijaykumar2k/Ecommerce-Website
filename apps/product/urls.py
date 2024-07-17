from django.urls import path

from apps.product import views
from apps.product.views import CreateProductView, ListProductView, ListProductViewJson, UpdateProductView, \
    DeleteProductView, CreateProductAddOnView, ListProductAddOnView, ListProductAddOnViewJson, \
    CreateProductAddOnOptionView, ListProductAddOnOptionView, ListProductAddOnOptionViewJson

urlpatterns = [
    path('admin/product/add', CreateProductView.as_view(), name='admin-product-add'),
    path('admin/product/list', ListProductView.as_view(), name='admin-product-list'),
    path('admin/product/list/ajax', ListProductViewJson.as_view(), name='admin-product-list-ajax'),
    path('admin/product/edit/<int:pk>', UpdateProductView.as_view(), name='admin-product-edit'),
    path('admin/product/delete/<int:pk>', DeleteProductView.as_view(), name='admin-product-delete'),
    path('upload/', views.upload_csv, name='upload_csv'),
    #addon
    path('admin/product/addon/<int:product_id>', CreateProductAddOnView.as_view(), name='admin-product-addon'),
    path('admin/productaddon/<int:product_id>', ListProductAddOnView.as_view(), name='admin-product-addon-list'),
    path('admin/productaddon/list/ajax', ListProductAddOnViewJson.as_view(), name='admin-product-addon-list-ajax'),
    #addon-option
    path('admin/product/addonoption/<int:productaddon_id>', CreateProductAddOnOptionView.as_view(), name='admin-product-addon-option'),
    path('admin/productaddonoption/<int:productaddon_id>', ListProductAddOnOptionView.as_view(), name='admin-product-addon-option-list'),
    path('admin/productaddonoption/list/ajax', ListProductAddOnOptionViewJson.as_view(), name='admin-product-addon-option-list-ajax'),

]
