from django.contrib import admin
from .models import MotherboardFormFactor, PsuFormFactor, MemoryType, CpuSocket, Vendor, MotherboardChipset, Case, Psu, Motherboard, Cpu, CpuCooler, Memory, GpuVendor, GpuType, Gpu, SsdType, Ssd, Hdd

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
    list_display = ('id', 'code', 'name', 'max_memory_frequency', 'memory_type', 'cpu_socket', 'created',)
    search_fields = ('name',)
    readonly_fields = ('created',)

@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'vendor', 'motherboard_form_factor', 'psu_form_factor', 'created',)
    search_fields = ('name',)
    readonly_fields = ('created',)

@admin.register(Psu)
class PsuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'vendor', 'watts', 'psu_form_factor', 'pcie_six_pin', 'pcie_eight_pin', 'created',)
    search_fields = ('name',)
    readonly_fields = ('created',)

@admin.register(Motherboard)
class MotherboardAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'vendor', 'motherboard_form_factor', 'chipset', 'ram_slots', 'm2_slots', 'created',)
    search_fields = ('name',)
    readonly_fields = ('created',)

@admin.register(Cpu)
class CpuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'vendor', 'cpu_socket', 'cores', 'threads', 'core_clock', 'boost_clock', 'tdp', 'graphics', 'created',)
    list_editable = ('name',)
    search_fields = ('name',)
    readonly_fields = ('created',)

@admin.register(CpuCooler)
class CpuCoolerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'vendor', 'fans', 'fan_size', 'created',)
    search_fields = ('name',)
    readonly_fields = ('created',)

@admin.register(Memory)
class MemoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'vendor', 'modules', 'size', 'frequency', 'type', 'cas', 'created',)
    list_editable = ('name', 'modules', 'size', 'frequency',)
    search_fields = ('name',)
    readonly_fields = ('created',)

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
    list_display = ('id', 'name', 'vendor', 'type', 'pcie_six_pin', 'pcie_eight_pin', 'created',)
    search_fields = ('name',)
    readonly_fields = ('created',)

@admin.register(SsdType)
class SsdTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name', 'created',)
    search_fields = ('name',)
    readonly_fields = ('created',)

@admin.register(Ssd)
class SsdAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'vendor', 'type', 'capacity', 'read_speed', 'write_speed', 'created',)
    search_fields = ('name',)
    readonly_fields = ('created',)

@admin.register(Hdd)
class SsdAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'vendor', 'format', 'capacity', 'created',)
    search_fields = ('name',)
    readonly_fields = ('created',)