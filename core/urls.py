from django.conf.urls import url, patterns


urlpatterns = patterns('core.views',
                       url(r'^$', 'index', name='index'),
                       url(r'^auth_return$', 'auth_return', name='return'),
)
