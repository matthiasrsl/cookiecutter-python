{% if cookiecutter.django_flavor == "drf" %}
from rest_framework.routers import DefaultRouter

from .views import ItemViewSet

router = DefaultRouter()
router.register("items", ItemViewSet)

urlpatterns = router.urls
{% elif cookiecutter.django_flavor == "ninja" %}
from django.urls import path

from .api import api

urlpatterns = [
    path("api/", api.urls),
]
{% else %}
from django.urls import path

from .views import health

urlpatterns = [
    path("health/", health, name="health"),
]
{% endif %}
