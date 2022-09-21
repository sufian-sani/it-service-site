"""itproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

# from django.contrib.sitemaps.views import sitemap
# from django.contrib import sitemaps

from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

# from .sitemaps import *

from django.contrib.sitemaps.views import sitemap
from django.urls import path

from mainapp.sitemaps import StaticViewSitemap, PostSitemap
# from . import views

sitemaps = {
    'static': StaticViewSitemap,
    'post': PostSitemap,
}


# from sitemaps import Static_Sitemap
# from notebooks.sitemaps import Article_Sitemap

# sitemaps = {
#     # 'article': Article_Sitemap(),
#     'static': Static_Sitemap(),
# }

# sitemaps = {
#     'posts': PostSitemap,
# }

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('mainapp.urls')),
    path('', include('digitalmarketing.urls')),
    path('sitemap', sitemap, {'sitemaps': sitemaps},name='django.contrib.sitemaps.views.sitemap'),
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)