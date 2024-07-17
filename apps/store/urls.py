from django.urls import path, include

from apps.store.views import CreateStoreView, ListStoreView, ListStoreViewJson, UpdateStoreView, DeleteStoreView

urlpatterns = [
    path('admin/store/add', CreateStoreView.as_view(), name='admin-store-add'),
    path('admin/store/list', ListStoreView.as_view(), name='admin-store-list'),
    path('admin/store/list/ajax', ListStoreViewJson.as_view(), name='admin-store-list-ajax'),
    path('admin/store/edit/<int:pk>', UpdateStoreView.as_view(), name='admin-store-edit'),
    path('admin/store/delete/<int:pk>', DeleteStoreView.as_view(), name='admin-store-delete'),
    path('rest_api/', include('apps.store.rest_api.urls')),

]