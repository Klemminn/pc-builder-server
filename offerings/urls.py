from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import Update

urlpatterns = format_suffix_patterns([
    path(
        'update/',
        Update.as_view(),
        name='update-offerings'
    ),
])
