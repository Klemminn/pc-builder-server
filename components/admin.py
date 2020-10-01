from django.contrib import admin
from .models import MotherboardFormFactor, PsuFormFactor, MemoryType, CpuSocket, Vendor, MotherboardChipset, Case, Motherboard, Cpu, CpuCooler, CpuCoolerSocketConnection, Memory, GpuVendor, GpuType, Gpu, StorageType, Storage


class MotherboardFormFactorAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name', 'created',)
    search_fields = ('name',)
    readonly_fields = ('created',)

admin.site.register(MotherboardFormFactor, MotherboardFormFactorAdmin)


class PsuFormFactorAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name', 'created',)
    search_fields = ('name',)
    readonly_fields = ('created',)

admin.site.register(PsuFormFactor, PsuFormFactorAdmin)


class MemoryTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name', 'created',)
    search_fields = ('name',)
    readonly_fields = ('created',)

admin.site.register(MemoryType, MemoryTypeAdmin)


class CpuSocketAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name', 'created',)
    search_fields = ('name',)
    readonly_fields = ('created',)

admin.site.register(CpuSocket, CpuSocketAdmin)


class VendorAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name', 'created',)
    search_fields = ('name',)
    readonly_fields = ('created',)

admin.site.register(Vendor, VendorAdmin)


class MotherboardChipsetAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name', 'max_memory_frequency', 'memory_type', 'cpu_socket', 'created',)
    search_fields = ('name',)
    readonly_fields = ('created',)

admin.site.register(MotherboardChipset, MotherboardChipsetAdmin)


class CaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'vendor', 'motherboard_form_factor', 'psu_form_factor', 'created',)
    search_fields = ('name',)
    readonly_fields = ('created',)

admin.site.register(Case, CaseAdmin)


class MotherboardAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'vendor', 'motherboard_form_factor', 'chipset', 'ram_slots', 'm2_slots', 'created',)
    search_fields = ('name',)
    readonly_fields = ('created',)

admin.site.register(Motherboard, MotherboardAdmin)


class CpuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'vendor', 'cpu_socket', 'cores', 'threads', 'core_clock', 'boost_clock', 'tdp', 'graphics', 'created',)
    search_fields = ('name',)
    readonly_fields = ('created',)

admin.site.register(Cpu, CpuAdmin)


class CpuCoolerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'vendor', 'fans', 'fan_size', 'created',)
    search_fields = ('name',)
    readonly_fields = ('created',)

admin.site.register(CpuCooler, CpuCoolerAdmin)


class CpuCoolerSocketConnectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'socket', 'cooler', 'created',)
    search_fields = ('name',)
    readonly_fields = ('created',)

admin.site.register(CpuCoolerSocketConnection, CpuCoolerSocketConnectionAdmin)


class MemoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'vendor', 'modules', 'frequency', 'type', 'cas', 'created',)
    search_fields = ('name',)
    readonly_fields = ('created',)

admin.site.register(Memory, MemoryAdmin)


class GpuVendorAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name', 'created',)
    search_fields = ('name',)
    readonly_fields = ('created',)

admin.site.register(GpuVendor, GpuVendorAdmin)


class GpuTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'vendor', 'created',)
    search_fields = ('name',)
    readonly_fields = ('created',)

admin.site.register(GpuType, GpuTypeAdmin)


class GpuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'vendor', 'type', 'memory', 'core_clock', 'boost_clock', 'tdp', 'created',)
    search_fields = ('name',)
    readonly_fields = ('created',)

admin.site.register(Gpu, GpuAdmin)


class StorageTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name', 'created',)
    search_fields = ('name',)
    readonly_fields = ('created',)

admin.site.register(StorageType, StorageTypeAdmin)


class StorageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'vendor', 'type', 'capacity', 'read_speed', 'write_speed', 'created',)
    search_fields = ('name',)
    readonly_fields = ('created',)

admin.site.register(Storage, StorageAdmin)
