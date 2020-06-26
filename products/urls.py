from django.conf.urls import url, include
from .views import all_products, filtered_products, sort_products
# from .views import all_products, filter_products

urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^(?P<category_name>[-\w]+)/$', filtered_products, name='filter'),
    url(r'^$', sort_products, name='sort'),
    ##url(r'^(?P<category_name>[-\w]+)/$', all_products, name='products'),
    # url(r'filter/?(category_name)', filter_products, name='filter'),
    # url(r'^cocktails_view/$', cocktails_view, name='cocktails_view'),
]
