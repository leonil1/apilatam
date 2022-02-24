from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from apps.store.models import Product
from apps.store.serializers import ProductModelSerializer


class ProductViewSet(mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    permission_classes = (IsAuthenticated, )
