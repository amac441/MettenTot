from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'blog.views.index'),
    url(r'^blog/', include('blog.urls'))
)
    #For more information on how to generate url patters, please view the official Django documentation.

    # Examples:
    # url(r'^$', 'MettenTot.views.home', name='home'),
    # url(r'^MettenTot/', include('MettenTot.MettenTot.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
