from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from depotapp.models import *
from depotapp import viewset
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from depotapp.views import login_view,logout_view

from django.contrib import admin
admin.autodiscover()

from rest_framework import routers, serializers, viewsets

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'order', viewset.OrderViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'depot.views.home', name='home'),
    # url(r'^depot/', include('depot.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
     (r'^accounts/login/$', login_view),
     (r'^accounts/logout/$', logout_view),
     url(r'^', include(router.urls)),
 #url(r'^restframework', include('djangorestframework.urls', namespace='djangorestframework')),
     url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)

urlpatterns += patterns ('',
 (r'^depotapp/', include('depotapp.urls')),

)

urlpatterns += staticfiles_urlpatterns()

