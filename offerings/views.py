from itertools import chain

from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_api_key.permissions import HasAPIKey
from django.contrib.contenttypes.models import ContentType
from django.db.models import Prefetch, Count, Min

from .models import Offering, Retailer
from components.models import Motherboard, Cpu, CpuCooler, Memory, Gpu, Ssd, Hdd, Case, Psu
from components.serializers import CpuSerializer, MemorySerializer, CpuCoolerSerializer, MotherboardSerializer, GpuSerializer, SsdSerializer, HddSerializer, CaseSerializer, PsuSerializer

def flatten(listable):
    return list(chain(*listable))

def get_common(model):
    components = model.objects.prefetch_related(Prefetch('offerings', queryset=Offering.objects.filter(disabled=False).order_by('price'))).filter(offerings__disabled=False)
    items = components.annotate(min_price=Min('offerings__price'))
    vendors = flatten(components.values_list('vendor__name').distinct())
    retailers = flatten(components.values_list('offerings__retailer__name').distinct())
    return {
        'components': components,
        'items': items.order_by('min_price'),
        'vendors': vendors,
        'retailers': retailers,
    }

class GetCpu(APIView):
    def get(self, request, format=None):
        common = get_common(Cpu)
        cpu_sockets = flatten(common.get('components').values_list('cpu_socket__name').distinct())
        return Response({
            'vendor': common.get('vendors'),
            'retailer': common.get('retailers'),
            'cpu_socket': cpu_sockets,
            'items': CpuSerializer(common.get('items'), many=True).data,
        })

class GetCpuCooler(APIView):
    def get(self, request, format=None):
        common = get_common(CpuCooler)
        fan_sizes = flatten(common.get('components').values_list('fan_size').order_by('fan_size').distinct())
        fans = flatten(common.get('components').values_list('fans').order_by('fans').distinct())
        return Response({
            'vendor': common.get('vendors'),
            'retailer': common.get('retailers'),
            'fans': fans,
            'fan_size': fan_sizes,
            'items': CpuCoolerSerializer(common.get('items'), many=True).data,
        })

class GetMotherboard(APIView):
    def get(self, request, format=None):
        common = get_common(Motherboard)
        cpu_sockets = flatten(common.get('components').values_list('chipset__cpu_socket__name').order_by('chipset__cpu_socket__name').distinct())
        chipsets = flatten(common.get('components').values_list('chipset__name').order_by('chipset__name').distinct())
        motherboard_form_factors = flatten(common.get('components').values_list('motherboard_form_factor__name').order_by('motherboard_form_factor__name').distinct())
        return Response({
            'vendor': common.get('vendors'),
            'retailer': common.get('retailers'),
            'cpu_socket': cpu_sockets,
            'chipset': chipsets,
            'motherboard_form_factor': motherboard_form_factors,
            'items': MotherboardSerializer(common.get('items'), many=True).data,
        })

class GetMemory(APIView):
    def get(self, request, format=None):
        common = get_common(Memory)
        types = flatten(common.get('components').values_list('type__name').distinct())
        frequency = flatten(common.get('components').values_list('frequency').order_by('frequency').distinct())
        sizes = flatten(common.get('components').values_list('size').order_by('size').distinct())
        return Response({
            'vendor': common.get('vendors'),
            'retailer': common.get('retailers'),
            'type': types,
            'frequency': frequency,
            'size': sizes,
            'items': MemorySerializer(common.get('items'), many=True).data,
        })

class GetGpu(APIView):
    def get(self, request, format=None):
        common = get_common(Gpu)
        types = flatten(common.get('components').values_list('type__name').order_by('type__name').distinct())
        return Response({
            'vendor': common.get('vendors'),
            'retailer': common.get('retailers'),
            'type': types,
            'items': GpuSerializer(common.get('items'), many=True).data,
        })

class GetSsd(APIView):
    def get(self, request, format=None):
        common = get_common(Ssd)
        types = flatten(common.get('components').values_list('type__name').order_by('type__name').distinct())
        capacity = flatten(common.get('components').values_list('capacity').order_by('capacity').distinct())
        return Response({
            'vendor': common.get('vendors'),
            'retailer': common.get('retailers'),
            'type': types,
            'capacity': capacity,
            'items': SsdSerializer(common.get('items'), many=True).data,
        })

class GetHdd(APIView):
    def get(self, request, format=None):
        common = get_common(Hdd)
        formats = flatten(common.get('components').values_list('format').order_by('format').distinct())
        capacity = flatten(common.get('components').values_list('capacity').order_by('capacity').distinct())
        return Response({
            'vendor': common.get('vendors'),
            'retailer': common.get('retailers'),
            'format': formats,
            'capacity': capacity,
            'items': HddSerializer(common.get('items'), many=True).data,
        })

class GetCase(APIView):
    def get(self, request, format=None):
        common = get_common(Case)
        motherboard_form_factors = flatten(common.get('components').values_list('motherboard_form_factor__name').order_by('motherboard_form_factor__name').distinct())
        psu_form_factors = flatten(common.get('components').values_list('psu_form_factor__name').order_by('psu_form_factor__name').distinct())
        return Response({
            'vendor': common.get('vendors'),
            'retailer': common.get('retailers'),
            'motherboard_form_factor': motherboard_form_factors,
            'psu_form_factor': psu_form_factors,
            'items': CaseSerializer(common.get('items'), many=True).data,
        })

class GetPsu(APIView):
    def get(self, request, format=None):
        common = get_common(Psu)
        psu_form_factors = flatten(common.get('components').values_list('psu_form_factor__name').order_by('psu_form_factor__name').distinct())
        watts = flatten(common.get('components').values_list('watts').order_by('watts').distinct())
        return Response({
            'vendor': common.get('vendors'),
            'retailer': common.get('retailers'),
            'psu_form_factor': psu_form_factors,
            'watts': watts,
            'items': PsuSerializer(common.get('items'), many=True).data,
        })

class Update(APIView):
    permission_classes = [HasAPIKey,]

    def post(self, request, format=None):
        items = request.data
        Offering.objects.update(disabled=True)
        for item in items:
            url = item.get('url')
            price = item.get('price')
            offering = Offering.objects.filter(url=url).first()
            if (offering is not None):
                offering.price = price
                offering.disabled = False
                offering.save()
                continue
            
            name = item.get('name')
            retailer_string = item.get('retailer')
            retailer = Retailer.objects.get(code=retailer_string)
            component = item.get('component')
            if (component == 'case'):
                content_type = ContentType.objects.get_for_model(Case)
            elif (component == 'psu'):
                content_type = ContentType.objects.get_for_model(Psu)
            elif (component == 'motherboard'):
                content_type = ContentType.objects.get_for_model(Motherboard)
            elif (component == 'cpu'):
                content_type = ContentType.objects.get_for_model(Cpu)
            elif (component == 'cooler'):
                content_type = ContentType.objects.get_for_model(CpuCooler)
            elif (component == 'memory'):
                content_type = ContentType.objects.get_for_model(Memory)
            elif (component == 'gpu'):
                content_type = ContentType.objects.get_for_model(Gpu)
            elif (component == 'ssd'):
                content_type = ContentType.objects.get_for_model(Ssd)
            elif (component == 'hdd'):
                content_type = ContentType.objects.get_for_model(Hdd)
            offering = Offering(
                name=name,
                url=url,
                price=price,
                retailer=retailer,
                content_type=content_type,
            )
            offering.save()
        return Response()
