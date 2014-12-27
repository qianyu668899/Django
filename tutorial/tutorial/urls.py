from django.conf.urls import patterns, include, url
from rest_framework import routers
from quickstart import views


from django.contrib import admin
admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tutorial.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^', include(router.urls)),
	url(r'^api_auth/', include('rest_framework.urls', namespace='rest_framework')),
	url(r'^', include('snippets.urls')),
	url(r'^snippets/$', views.snippet_list),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
)
