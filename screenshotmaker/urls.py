from django.conf.urls import patterns, include, url
from screenshotmaker import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

print settings.STATICFILES_DIR

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'screenshotmaker.views.home', name='home'),
    # url(r'^screenshotmaker/', include('screenshotmaker.foo.urls')),

    url(r'', include('app.urls')),
    url(r'^resources/(?P<path>.*)', 'django.views.static.serve', {
      'document_root': settings.STATICFILES_DIR
    }),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
