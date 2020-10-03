from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_api_key.permissions import HasAPIKey
from django.contrib.contenttypes.models import ContentType

from .models import Offering, Retailer
from components.models import Case, Psu, Motherboard, Cpu, CpuCooler, Memory, Gpu, Storage

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
                break
            
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
            elif (component == 'storage'):
                content_type = ContentType.objects.get_for_model(Storage)
            offering = Offering(
                name=name,
                url=url,
                price=price,
                retailer=retailer,
                content_type=content_type,
            )
            offering.save()
        return Response()

# {'retailer': 'att', 'url': 'https://att.is/product/msi-x399-sli-plus-modurbord', 'component': 'motherboard', 'name': 'MSI X399 SLI Plus  mÃ³Ã°urborÃ°', 'price': 61950}
