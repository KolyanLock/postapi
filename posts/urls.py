from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

urlpatterns = router.urls
