from django.conf.urls import url
from .views import about

urlpatterns = [
        url(r'^about/$', about, name='about'),
]
