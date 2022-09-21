from django.contrib import admin
from django.urls import include, re_path, path

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^', include('download.urls')),
]
