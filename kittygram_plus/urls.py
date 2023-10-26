from django.urls import include, path
from rest_framework.routers import DefaultRouter

from cats.views import CatViewSet, LightCatViewSet, OwnerViewSer

router = DefaultRouter()
router.register('cats', CatViewSet)
router.register('owners', OwnerViewSer)
router.register(r'mycats', LightCatViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
