from django.urls import path
from apps.banner.views import CreateBannerView, ListBannerView, ListBannerViewJson, UpdateBannerView, DeleteBannerView

urlpatterns = [
    path('admin/banner/add', CreateBannerView.as_view(), name='admin-banner-add'),
    path('admin/banner/list', ListBannerView.as_view(), name='admin-banner-list'),
    path('admin/banner/list/ajax', ListBannerViewJson.as_view(), name='admin-banner-list-ajax'),
    path('admin/banner/edit/<int:pk>', UpdateBannerView.as_view(), name='admin-banner-edit'),
    path('admin/banner/delete/<int:pk>', DeleteBannerView.as_view(), name='admin-banner-delete'),
]