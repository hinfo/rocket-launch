from django.conf.urls import url, patterns, include
from django.contrib import admin
from django.conf import settings
# from django.conf import static

urlpatterns = patterns('',
                       url(r'^', include('core.urls', namespace='core')),
                       url(r'^admin/', include(admin.site.urls)),
)
