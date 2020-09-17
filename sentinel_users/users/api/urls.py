from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from sentinel_users.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("", UserViewSet)

urlpatterns = router.urls
