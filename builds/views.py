import re
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.contenttypes.models import ContentType
from django.db.models import Prefetch, Count, Min

from .models import Build
from offerings.models import Offering
from components.serializers import CpuSerializer, CpuCoolerSerializer, MotherboardSerializer, MemorySerializer, GpuSerializer, SsdSerializer, HddSerializer, CaseSerializer, PsuSerializer
from offerings.serializers import OfferingSerializer

component_serializers = {
    'cpu': CpuSerializer,
    'cpu_cooler': CpuCoolerSerializer,
    'motherboard': MotherboardSerializer,
    'memory': MemorySerializer,
    'gpu': GpuSerializer,
    'ssd': SsdSerializer,
    'hdd': HddSerializer,
    'case': CaseSerializer,
    'psu': PsuSerializer
}

def model_to_snake(model):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', model.__name__).lower()

class GetBuild(APIView):
    def get(self, request, format=None, **kwargs):
        code = kwargs.get('code')
        build = Build.objects.get(code=code)
        offerings = Offering.objects.filter(id__in=build.offerings)
        response = {
            'build_id': kwargs.get('code'),
        }
        for offering in offerings:
            component = offering.content_object
            model = type(component)
            component_type = model_to_snake(model)

            full_component = model.objects.prefetch_related(Prefetch('offerings', queryset=Offering.objects.order_by('price'))).annotate(min_price=Min('offerings__price')).get(id=component.id)

            component_serialized = component_serializers[component_type](full_component)
            extended_data = { 'selected_offering': OfferingSerializer(offering).data }
            extended_data.update(component_serialized.data)

            response[component_type] = extended_data

        return Response(response)

class CreateBuild(APIView):
    def post(self, request, format=None):
        offerings = request.data
        (build, created,) = Build.objects.get_or_create(offerings=offerings)

        return Response(build.code)