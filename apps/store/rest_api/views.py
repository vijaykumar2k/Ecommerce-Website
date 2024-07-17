from rest_framework import viewsets

from apps.store.models import Store
from apps.store.rest_api.serializers import StoreSerializer

class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
