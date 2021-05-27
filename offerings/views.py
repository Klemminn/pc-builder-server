from itertools import chain

from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_api_key.permissions import HasAPIKey
from django.contrib.contenttypes.models import ContentType
from django.db.models import Prefetch, Count, Min

from .models import Offering, Retailer, Scrape
from components.models import Monitor, Motherboard, Cpu, CpuCooler, Memory, Gpu, Ssd, Hdd, Case, Psu
from components.serializers import CpuSerializer, MemorySerializer, CpuCoolerSerializer, MonitorSerializer, MotherboardSerializer, GpuSerializer, SsdSerializer, HddSerializer, CaseSerializer, PsuSerializer

def flatten(listable):
    return list(chain(*listable))

def get_distinct_property(components, property):
    return flatten(components.values_list(property).order_by(property).distinct())

def get_common(model):
    components = model.objects.prefetch_related(Prefetch('offerings', queryset=Offering.objects.filter(disabled=False).filter(ignored=False).order_by('price'))).filter(offerings__disabled=False)
    items = components.annotate(min_price=Min('offerings__price'))
    vendors = get_distinct_property(components, 'vendor__name')
    retailers = get_distinct_property(components, 'offerings__retailer__name')
    return {
        'components': components,
        'items': items.order_by('min_price'),
        'vendors': vendors,
        'retailers': retailers,
    }

class GetCpu(APIView):
    def get(self, request, format=None):
        common = get_common(Cpu)
        cpu_sockets = get_distinct_property(common.get('components'), 'cpu_socket__name')
        return Response({
            'vendor': common.get('vendors'),
            'retailer': common.get('retailers'),
            'cpu_socket': cpu_sockets,
            'items': CpuSerializer(common.get('items'), many=True).data,
        })

class GetCpuCooler(APIView):
    def get(self, request, format=None):
        common = get_common(CpuCooler)
        fan_sizes = get_distinct_property(common.get('components'), 'fan_size')
        fans = get_distinct_property(common.get('components'), 'fans')
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
        cpu_sockets = get_distinct_property(common.get('components'), 'chipset__cpu_socket__name')
        chipsets = get_distinct_property(common.get('components'), 'chipset__name')
        motherboard_form_factors = get_distinct_property(common.get('components'), 'motherboard_form_factor__name')
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
        types = get_distinct_property(common.get('components'), 'type__name')
        frequency = get_distinct_property(common.get('components'), 'frequency')
        sizes = get_distinct_property(common.get('components'), 'size')
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
        types = get_distinct_property(common.get('components'), 'type__name')
        return Response({
            'vendor': common.get('vendors'),
            'retailer': common.get('retailers'),
            'type': types,
            'items': GpuSerializer(common.get('items'), many=True).data,
        })

class GetSsd(APIView):
    def get(self, request, format=None):
        common = get_common(Ssd)
        types = get_distinct_property(common.get('components'), 'type__name')
        capacity = get_distinct_property(common.get('components'), 'capacity')
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
        formats = get_distinct_property(common.get('components'), 'format')
        capacity = get_distinct_property(common.get('components'), 'capacity')
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
        motherboard_form_factors = get_distinct_property(common.get('components'), 'motherboard_form_factor__name')
        psu_form_factors = get_distinct_property(common.get('components'), 'psu_form_factor__name')
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
        psu_form_factors = get_distinct_property(common.get('components'), 'psu_form_factor__name')
        # We do ratings manually here, instead of using get_distinct, since we want to filter out the null result
        ratings = flatten(common.get('components').filter(rating__isnull=False).values_list('rating').order_by('rating').distinct())
        watts = get_distinct_property(common.get('components'), 'watts')
        return Response({
            'vendor': common.get('vendors'),
            'retailer': common.get('retailers'),
            'psu_form_factor': psu_form_factors,
            'watts': watts,
            'rating': ratings,
            'items': PsuSerializer(common.get('items'), many=True).data,
        })

class GetMonitor(APIView):
    def get(self, request, format=None):
        common = get_common(Monitor)
        resolutions = get_distinct_property(common.get('components'), 'resolution__resolution')
        panels = get_distinct_property(common.get('components'), 'panel__panel')
        refresh_rates = get_distinct_property(common.get('components'), 'refresh_rate')
        sizes = get_distinct_property(common.get('components'), 'size')
        # We do freesync and gsync manually, instead of using get_distinct, since we want to filter out the null result
        freesync = flatten(common.get('components').filter(freesync__isnull=False).values_list('freesync').order_by('freesync').distinct())
        gsync = flatten(common.get('components').filter(gsync__isnull=False).values_list('gsync').order_by('gsync').distinct())
        return Response({
            'vendor': common.get('vendors'),
            'retailer': common.get('retailers'),
            'resolution': resolutions,
            'size': sizes,
            'panel': panels,
            'freesync': freesync,
            'gsync': gsync,
            'refresh_rate': refresh_rates,
            'items': MonitorSerializer(common.get('items'), many=True).data,
        })

class Update(APIView):
    permission_classes = [HasAPIKey,]

    def post(self, request, format=None):
        items = request.data
        total_offerings_count = len(items)
        Offering.objects.update(disabled=True)
        new_offerings_count = 0
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
            elif (component == 'monitor'):
                content_type = ContentType.objects.get_for_model(Monitor)
            offering = Offering(
                name=name,
                url=url,
                price=price,
                retailer=retailer,
                content_type=content_type,
            )
            offering.save()
            new_offerings_count += 1

        scrape_instance = Scrape(
            new_offerings=new_offerings_count,
            total_offerings=total_offerings_count
        )
        scrape_instance.save()
        return Response()
