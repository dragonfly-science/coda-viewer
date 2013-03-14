from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^api.v0/(?P<dataset>.*)/data/(?P<variable>.*)', 'codavisualiser.api.v0.get_data'),

    url(r'^(?P<dataset>.*)/variables$', 'codavisualiser.views.variables'),
    url(r'^(?P<dataset>.*)/overview$', 'codavisualiser.views.overview'),
    url(r'^(?P<dataset>.*)/trace/(?P<variable>.*)$', 'codavisualiser.views.trace'),
    # Examples:
    # url(r'^$', 'codaviewer.views.home', name='home'),
    # url(r'^codaviewer/', include('codaviewer.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
