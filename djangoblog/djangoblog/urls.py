from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from blogpages.sitemaps import PostSitemap

sitemaps = {
    "posts": PostSitemap,
}
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blogpages.urls')),
    path('stem_workshops/', include('stem_workshops.urls')),
    path('summernote/', include('django_summernote.urls')),
]
