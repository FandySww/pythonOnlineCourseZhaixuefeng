from django.conf.urls import url
from dorun.views import indexOnline, indexOnlinelocal,indexOffline,indexOfflinelocal

urlpatterns = [
    url(r'^runShellOnline/$', indexOnline),
    url(r'^runShellOffline/$', indexOffline),
    url(r'^runShellOnlinelocal/$', indexOnlinelocal),
    url(r'^runShellOfflinelocal/$', indexOfflinelocal),
]
