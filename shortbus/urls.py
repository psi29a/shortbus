from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

from djangobb_forum import settings as forum_settings
from sitemap import SitemapForum, SitemapTopic

from shortbus.home import views

admin.autodiscover()

sitemaps = {
    'forum': SitemapForum,
    'topic': SitemapTopic,
}

urlpatterns = patterns('',
    # Landing page
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    
    # Shortbus Field
    (r'^field/$', include('shortbus.field.urls', namespace='field')),

    # Admin
    (r'^admin/', include(admin.site.urls)),

    # Sitemap
    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),

    # Apps
    (r'^accounts/', include('allauth.urls')),
    (r'^forum/', include('djangobb_forum.urls', namespace='djangobb')),
    
)

# PM Extension
if (forum_settings.PM_SUPPORT):
    urlpatterns += patterns('',
        (r'^forum/pm/', include('django_messages.urls')),
   )
    
if (settings.DEBUG):
    urlpatterns += patterns('',
        (r'^%s(?P<path>.*)$' % settings.MEDIA_URL.lstrip('/'),
            'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )    
