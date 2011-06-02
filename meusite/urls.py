from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^hello/$', 'eventos.views.hello'),
    # Examples:
    # url(r'^$', 'meusite.views.home', name='home'),
    # url(r'^meusite/', include('meusite.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
