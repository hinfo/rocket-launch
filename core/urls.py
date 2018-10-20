from django.conf.urls import url, patterns


urlpatterns = patterns('core.views',
                       url(r'^$', 'index', name='index'),
)