from django.urls import path, include
from .views import meinXoevStandard_list, meinXoevStandard_list_kern, MeinXOEVStandardViewSet
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

router = DefaultRouter()
router.register("api/meinXOEVStandard", MeinXOEVStandardViewSet, basename="meinXOEVStandard")

urlpatterns = [
    path("", meinXoevStandard_list, name="meinXoevStandard_list"),
    path("kern", meinXoevStandard_list_kern, name="meinXoevStandard_list_kern"),
    path("kerndemo", TemplateView.as_view(template_name="kerndemo.html"), name="kerndemo"),
    path("", include(router.urls)),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
]