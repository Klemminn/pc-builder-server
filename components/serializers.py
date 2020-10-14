from rest_framework import serializers
from .models import Cpu, CpuCooler, Motherboard, Memory, Gpu, Ssd, Hdd, Case, Psu
from offerings.serializers import OfferingSerializer

class CpuSerializer(serializers.ModelSerializer):
    vendor = serializers.ReadOnlyField(source='vendor.name')
    cpu_socket = serializers.ReadOnlyField(source='cpu_socket.name')
    offerings = OfferingSerializer(many=True, read_only=True)
    min_price = serializers.IntegerField()
    class Meta:
        model = Cpu
        fields = ('id', 'vendor', 'name', 'cpu_socket', 'cores', 'threads', 'core_clock', 'boost_clock', 'tdp', 'graphics', 'image', 'min_price', 'offerings',)

class CpuCoolerSerializer(serializers.ModelSerializer):
    vendor = serializers.ReadOnlyField(source='vendor.name')
    offerings = OfferingSerializer(many=True, read_only=True)
    min_price = serializers.IntegerField()

    class Meta:
        model = CpuCooler
        fields = ('id', 'vendor', 'name', 'fans', 'fan_size', 'image', 'min_price', 'offerings',)

class MotherboardSerializer(serializers.ModelSerializer):
    vendor = serializers.ReadOnlyField(source='vendor.name')
    motherboard_form_factor = serializers.ReadOnlyField(source='motherboard_form_factor.name')
    cpu_socket = serializers.ReadOnlyField(source='chipset.cpu_socket.name')
    chipset = serializers.ReadOnlyField(source='chipset.name')
    offerings = OfferingSerializer(many=True, read_only=True)
    min_price = serializers.IntegerField()
    class Meta:
        model = Motherboard
        fields = ('id', 'vendor', 'name', 'motherboard_form_factor', 'cpu_socket', 'chipset', 'ram_slots', 'm2_slots', 'image', 'min_price', 'offerings',)

class MemorySerializer(serializers.ModelSerializer):
    vendor = serializers.ReadOnlyField(source='vendor.name')
    type = serializers.ReadOnlyField(source='type.name')
    offerings = OfferingSerializer(many=True, read_only=True)
    min_price = serializers.IntegerField()

    class Meta:
        model = Memory
        fields = ('id', 'vendor', 'name', 'frequency', 'type', 'modules', 'size', 'cas', 'image', 'min_price', 'offerings',)

class GpuSerializer(serializers.ModelSerializer):
    vendor = serializers.ReadOnlyField(source='vendor.name')
    type = serializers.ReadOnlyField(source='type.name')
    offerings = OfferingSerializer(many=True, read_only=True)
    min_price = serializers.IntegerField()

    class Meta:
        model = Gpu
        fields = ('id', 'vendor', 'name', 'type', 'pcie_six_pin', 'pcie_eight_pin', 'image', 'min_price', 'offerings',)

class SsdSerializer(serializers.ModelSerializer):
    vendor = serializers.ReadOnlyField(source='vendor.name')
    type = serializers.ReadOnlyField(source='type.name')
    offerings = OfferingSerializer(many=True, read_only=True)
    min_price = serializers.IntegerField()

    class Meta:
        model = Ssd
        fields = ('id', 'vendor', 'name', 'type', 'capacity', 'read_speed', 'write_speed', 'image', 'min_price', 'offerings',)

class HddSerializer(serializers.ModelSerializer):
    vendor = serializers.ReadOnlyField(source='vendor.name')
    offerings = OfferingSerializer(many=True, read_only=True)
    min_price = serializers.IntegerField()

    class Meta:
        model = Hdd
        fields = ('id', 'vendor', 'name', 'format', 'capacity', 'image', 'min_price', 'offerings',)

class CaseSerializer(serializers.ModelSerializer):
    vendor = serializers.ReadOnlyField(source='vendor.name')
    motherboard_form_factor = serializers.ReadOnlyField(source='motherboard_form_factor.name')
    psu_form_factor = serializers.ReadOnlyField(source='psu_form_factor.name')
    offerings = OfferingSerializer(many=True, read_only=True)
    min_price = serializers.IntegerField()

    class Meta:
        model = Case
        fields = ('id', 'vendor', 'name', 'motherboard_form_factor', 'psu_form_factor', 'image', 'min_price', 'offerings',)

class PsuSerializer(serializers.ModelSerializer):
    vendor = serializers.ReadOnlyField(source='vendor.name')
    psu_form_factor = serializers.ReadOnlyField(source='psu_form_factor.name')
    offerings = OfferingSerializer(many=True, read_only=True)
    min_price = serializers.IntegerField()

    class Meta:
        model = Psu
        fields = ('id', 'vendor', 'name', 'watts', 'psu_form_factor', 'rating', 'pcie_six_pin', 'pcie_eight_pin', 'image', 'min_price', 'offerings',)