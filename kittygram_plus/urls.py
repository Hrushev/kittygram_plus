from django.urls import include, path

from rest_framework.routers import DefaultRouter

from cats.views import CatViewSet, OwnerViewSer


router = DefaultRouter()
router.register('cats', CatViewSet)
router.register('owners', OwnerViewSer)

urlpatterns = [
    path('', include(router.urls)),
]
