from django.conf.urls import patterns, include, url
from oscar.app import application

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myshop.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include(application.urls)),
)
