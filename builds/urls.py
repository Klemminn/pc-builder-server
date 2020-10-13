from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import GetBuild, CreateBuild

urlpatterns = format_suffix_patterns([
     path(
        r'<str:code>',
        GetBuild.as_view(),
        name='get-build'
    ),
    path(
        'create/',
        CreateBuild.as_view(),
        name='create-build'
    ),
])
