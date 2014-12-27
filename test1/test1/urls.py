from django.conf.urls import patterns, include, url
from test1.views import current_datetime
from test1.views import hours_ahead
from book.views import search

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'test1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	(r'^yutime/$', current_datetime),
	(r'^time/plus/(\d{1,2})/$', hours_ahead),
	#(r'^admin/', include('django.contrib.admin.urls')),
	(r'^search/$',search),
	(r'^contact/$', 'book.views.contact'),
	(r'^add_publisher/$', 'book.views.add_publisher'),
	(r'^polls/', include('polls.urls', namespace='polls')),
)
