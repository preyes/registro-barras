from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


admin.autodiscover()

urlpatterns = patterns('',

    url(r'^qbe/', include('django_qbe.urls')),
    url(r'^lector/','barras.views.guardar_codigo'),
    url(r'^reporte/','barras.views.report_view'),
    url(r'^index/','barras.views.index'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
		{'document_root':settings.MEDIA_ROOT,}
        ),



)

