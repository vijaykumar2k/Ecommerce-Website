from django.urls import include, path
from rest_framework import routers

from apps.store.rest_api.views import StoreViewSet

router = routers.DefaultRouter()
router.register(r'store',StoreViewSet)


urlpatterns = [
    path('',include(router.urls))
]