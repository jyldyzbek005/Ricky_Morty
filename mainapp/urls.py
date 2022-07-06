
from rest_framework.routers import DefaultRouter
from .views import LocationViewSet, CharacterViewSet, EpizodeViewSet
from .views import *

router = DefaultRouter()

router.register('location', LocationViewSet)
router.register('character', CharacterViewSet)
router.register('epizode', EpizodeViewSet)

urlpatterns = router.urls