from django.urls import include, path

from .v1.urls import v1_urls

api_urls = [
    path("", include(v1_urls)),
]
