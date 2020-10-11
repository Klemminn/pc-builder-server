from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import Update, GetCpu, GetMemory, GetCpuCooler, GetGpu, GetSsd, GetHdd, GetCase, GetPsu

urlpatterns = format_suffix_patterns([
    path(
        'update/',
        Update.as_view(),
        name='update-offerings'
    ),
    path(
        'cpu/',
        GetCpu.as_view(),
        name='get-cpus'
    ),
    path(
        'cpuCooler/',
        GetCpuCooler.as_view(),
        name='get-cpu-cooler'
    ),
    path(
        'memory/',
        GetMemory.as_view(),
        name='get-memory'
    ),
    path(
        'gpu/',
        GetGpu.as_view(),
        name='get-gpu'
    ),
    path(
        'ssd/',
        GetSsd.as_view(),
        name='get-ssd'
    ),
    path(
        'hdd/',
        GetHdd.as_view(),
        name='get-hdd'
    ),
    path(
        'case/',
        GetCase.as_view(),
        name='get-case'
    ),
    path(
        'psu/',
        GetPsu.as_view(),
        name='get-psu'
    ),
])
