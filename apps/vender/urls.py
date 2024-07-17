from django.urls import path

from apps.vender.views import CreateVenderView, ListVenderView, ListVenderViewJson, UpdateVenderView, DeleteVenderView

urlpatterns = [
    path('admin/vender/add', CreateVenderView.as_view(), name='admin-vender-add'),
    path('admin/vender/list', ListVenderView.as_view(), name='admin-vender-list'),
    path('admin/vender/list/ajax', ListVenderViewJson.as_view(), name='admin-vender-list-ajax'),
    path('admin/vender/edit/<int:pk>', UpdateVenderView.as_view(), name='admin-vender-edit'),
    path('admin/vender/delete/<int:pk>', DeleteVenderView.as_view(), name='admin-vender-delete'),
]