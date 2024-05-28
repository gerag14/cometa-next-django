from django.contrib import admin
from django.urls import include, path
from onlybeer.api.urls import api_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(api_urls)),
]
