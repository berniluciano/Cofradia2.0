"""miprimersitio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
from login.views import Register
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^login/$', 'login.views.login_page', name='login'),
    url(r'^logout/$', 'login.views.logout_page', name='logout'),
    url(r'^register/$', Register.as_view(), name='register'),
    url(r'^$', 'login.views.homepage', name='homepage'),
    url(r'^publi/(?P<publi_id>\d+)/$', 'aplicacion.views.publi_detalle', name='publi_detalle'),


]
