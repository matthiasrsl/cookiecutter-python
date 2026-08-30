{% if cookiecutter.django_flavor == "drf" %}
from rest_framework import viewsets

from .models import Item
from .serializers import ItemSerializer


class ItemViewSet(viewsets.ModelViewSet[Item]):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
{% elif cookiecutter.django_flavor == "plain" %}
from django.http import HttpRequest, JsonResponse
from django.views.decorators.http import require_GET


@require_GET
def health(request: HttpRequest) -> JsonResponse:
    return JsonResponse({"status": "ok"})
{% endif %}
