from apps.advert.models import Advert
from apps.advert.serializers.response import (
    AdvertDetailSerializer,
    AdvertListSerializer,
)
from django.db import transaction
from django.db.models import F
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
)


class AdvertListApiView(ListAPIView):
    serializer_class = AdvertListSerializer
    queryset = Advert.objects.select_related('category', 'city').order_by('-created')


class AdvertRetrieveApiView(RetrieveAPIView):
    serializer_class = AdvertDetailSerializer
    queryset = Advert.objects.select_related('category', 'city').filter()

    def get_object(self):
        filter_kwargs = {self.lookup_field: self.kwargs[self.lookup_field]}

        with transaction.atomic():
            instance = self.queryset.select_for_update().get(**filter_kwargs)

            instance.views = F('views') + 1
            instance.save(update_fields=['views'])

            instance.refresh_from_db()
        return instance
