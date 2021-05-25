from django.contrib import admin
from django.utils.html import format_html
from .models import MotherboardFormFactor, PsuFormFactor, MemoryType, CpuSocket, Vendor, MotherboardChipset, Case, Psu, Motherboard, Cpu, CpuCooler, Memory, GpuVendor, GpuType, Gpu, SsdType, Ssd, Hdd

def get_offerings_links(obj):
    return format_html(", ".join([format_html("<a href='{url}' target='_blank'>{retailer}</a>", url=k.url, retailer=k.retailer) for k in obj.offerings.filter(disabled=False)]))

@admin.register(MotherboardFormFactor)
class MotherboardFormFactorAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name', 'created',)
    search_fields = ('name',)
    readonly_fields = ('created',)

@admin.register(PsuFormFactor)
class PsuFormFactorAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name', 'created',)
    search_fields = ('name',)
    readonly_fields = ('created',)

@admin.register(MemoryType)
class MemoryTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name', 'created',)
    search_fields = ('name',)
    readonly_fields = ('created',)

@admin.register(CpuSocket)
class CpuSocketAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name', 'created',)
    search_fields = ('name',)
    readonly_fields = ('created',)

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name', 'created',)
    search_fields = ('name',)
    readonly_fields = ('created',)

@admin.register(MotherboardChipset)
class MotherboardChipsetAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name', 'memory_type', 'cpu_socket', 'created',)
    search_fields = ('name',)
    readonly_fields = ('created',)

@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'vendor', 'motherboard_form_factor', 'psu_form_factor', 'offerings', 'created',)
    search_fields = ('name',)
    readonly_fields = ('created',)

    def offerings(self, obj):
        return get_offerings_links(obj)

@admin.register(Psu)
class PsuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'vendor', 'watts', 'rating', 'psu_form_factor', 'pcie_six_pin', 'pcie_eight_pin', 'offerings', 'created',)
    search_fields = ('name',)
    readonly_fields = ('created',)

    def offerings(self, obj):
        return get_offerings_links(obj)

@admin.register(Motherboard)
class MotherboardAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'vendor', 'motherboard_form_factor', 'chipset', 'ram_slots', 'm2_slots', 'offerings', 'created',)
    search_fields = ('name',)
    readonly_fields = ('created',)

    def offerings(self, obj):
        return get_offerings_links(obj)

@admin.register(Cpu)
class CpuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'vendor', 'cpu_socket', 'cores', 'threads', 'core_clock', 'boost_clock', 'tdp', 'graphics', 'offerings', 'created',)
    list_editable = ('name',)
    search_fields = ('name',)
    readonly_fields = ('created',)

    def offerings(self, obj):
        return get_offerings_links(obj)

@admin.register(CpuCooler)
class CpuCoolerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'vendor', 'fans', 'fan_size', 'offerings', 'created',)
    search_fields = ('name',)
    readonly_fields = ('created',)

    def offerings(self, obj):
        return get_offerings_links(obj)

@admin.register(Memory)
class MemoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'vendor', 'modules', 'size', 'frequency', 'type', 'cas', 'offerings', 'created',)
    list_editable = ('name', 'modules', 'size', 'frequency',)
    search_fields = ('name',)
    readonly_fields = ('created',)

    def offerings(self, obj):
        return get_offerings_links(obj)

@admin.register(GpuVendor)
class GpuVendorAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name', 'created',)
    search_fields = ('name',)
    readonly_fields = ('created',)

@admin.register(GpuType)
class GpuTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'vendor', 'created',)
    search_fields = ('name',)
    readonly_fields = ('created',)

@admin.register(Gpu)
class GpuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'vendor', 'type', 'pcie_six_pin', 'pcie_eight_pin', 'offerings', 'created',)
    search_fields = ('name',)
    readonly_fields = ('created',)

    def offerings(self, obj):
        return get_offerings_links(obj)

@admin.register(SsdType)
class SsdTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name', 'created',)
    search_fields = ('name',)
    readonly_fields = ('created',)

@admin.register(Ssd)
class SsdAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'vendor', 'type', 'capacity', 'read_speed', 'write_speed', 'offerings', 'created',)
    search_fields = ('name',)
    readonly_fields = ('created',)

    def offerings(self, obj):
        return get_offerings_links(obj)

@admin.register(Hdd)
class HddAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'vendor', 'format', 'capacity', 'offerings', 'created',)
    search_fields = ('name',)
    readonly_fields = ('created',)

    def offerings(self, obj):
        return get_offerings_links(obj)