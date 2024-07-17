from django.urls import path
from apps.category.views import ListCategoryView, ListCategoryViewJson, CreateCategoryView, DeleteCategoryView, \
    UpdateCategoryView


urlpatterns = [
    path('admin/category/add', CreateCategoryView.as_view(), name='admin-category-add'),
    path('admin/category/list', ListCategoryView.as_view(), name='admin-category-list'),
    path('admin/category/list/ajax', ListCategoryViewJson.as_view(), name='admin-category-list-ajax'),
    path('admin/category/edit/<int:pk>', UpdateCategoryView.as_view(), name='admin-category-edit'),
    path('admin/category/delete/<int:pk>', DeleteCategoryView.as_view(), name='admin-category-delete')

]