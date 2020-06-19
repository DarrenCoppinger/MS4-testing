from django.conf.urls import url, include
from .views import all_products, filter_products

urlpatterns = [
    url(r'^all/$', all_products, name='products'),
    url(r'^filter/(?P<category>[\w-]+)$', filter_products, name='filter'),
]
