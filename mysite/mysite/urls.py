from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('homepage.urls')),
    url(r'^research/', include('research.urls')),
    url(r'^executive/', include('executive.urls')),
    url(r'^executive/dbexec/', include('dbexec.urls')),
    url(r'^unitdirector/', include('unitdirector.urls')),
]
