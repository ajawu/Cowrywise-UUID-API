from .views import UUIDTimeViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('', UUIDTimeViewSet, basename='uuid')
urlpatterns = router.urls
