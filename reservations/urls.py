from django.conf.urls import url
from .views import reservation

urlpatterns = [
    url(r'^$', reservation, name='reservation'),
]