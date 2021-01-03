from django.conf.urls import url
from dorun.views import index
urlpatterns = [
    url(r'^runshell/$',index),
]