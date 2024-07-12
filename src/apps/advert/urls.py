from django.urls import path

from apps.advert.views import (
    AdvertListApiView,
    AdvertRetrieveApiView,
)

urlpatterns = [
    path('<uuid:pk>', AdvertRetrieveApiView.as_view(), name='news-id'),
    path('list', AdvertListApiView.as_view(), name='news-id')
]
