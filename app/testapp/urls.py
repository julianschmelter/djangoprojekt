from django.urls import path
from .views import meinXoevStandard_list, meinXoevStandard_list_kern
from django.views.generic import TemplateView

urlpatterns = [
path("", meinXoevStandard_list, name="meinXoevStandard_list"),
path("kern", meinXoevStandard_list_kern, name="meinXoevStandard_list_kern"),
path("kerndemo", TemplateView.as_view(template_name="kerndemo.html"), name="kerndemo"),
]