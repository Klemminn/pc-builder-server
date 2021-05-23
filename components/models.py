from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from builder.validators import validate_image_extension
from builder.utils import handle_upload

from offerings.models import Offering

def ImageField():
    return models.ImageField(
        upload_to=handle_upload,
        validators=[validate_image_extension],
    )

class MotherboardFormFactor(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)

    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('name',)


class PsuFormFactor(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)

    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class MemoryType(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)

    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('name',)


class CpuSocket(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)

    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=10)

    def __str__(self):
        return '%s - %s' % (self.code, self.name,)
    
    class Meta:
        ordering = ('name',)


class Vendor(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)

    code = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('name',)
    

class MotherboardChipset(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)

    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=10)
    memory_type = models.ForeignKey(MemoryType, related_name='motherboard_chipsets', to_field='code', on_delete=models.CASCADE)
    cpu_socket = models.ForeignKey(CpuSocket, related_name='motherboard_chipsets', to_field='code', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('name',)


class Cpu(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)

    name = models.CharField(max_length=100)
    vendor = models.ForeignKey(Vendor, related_name='cpus', to_field='code', on_delete=models.CASCADE)
    cpu_socket = models.ForeignKey(CpuSocket, related_name='cpus', to_field='code', on_delete=models.CASCADE)
    cores = models.IntegerField(default=6)
    threads = models.IntegerField(default=6)
    core_clock = models.IntegerField()
    boost_clock = models.IntegerField(null=True, blank=True)
    tdp = models.IntegerField()
    graphics = models.CharField(null=True, blank=True, max_length=30)
    image = ImageField()
    offerings = GenericRelation(Offering)

    def __str__(self):
        return '%s. %s - %s' % (self.id, self.cpu_socket, self.name,)


class CpuCooler(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)

    name = models.CharField(max_length=100, unique=True)
    vendor = models.ForeignKey(Vendor, related_name='cpu_coolers', to_field='code', on_delete=models.CASCADE)
    fans = models.IntegerField(default=1)
    fan_size = models.IntegerField(default=120)
    image = ImageField()
    offerings = GenericRelation(Offering)

    def __str__(self):
        return '%s. %s' % (self.id, self.name,)


class Motherboard(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)

    name = models.CharField(max_length=100)
    vendor = models.ForeignKey(Vendor, related_name='motherboards', to_field='code', on_delete=models.CASCADE)
    motherboard_form_factor = models.ForeignKey(MotherboardFormFactor, related_name='motherboards', to_field='code', on_delete=models.CASCADE)
    chipset = models.ForeignKey(MotherboardChipset, related_name='motherboards', to_field='code', on_delete=models.CASCADE)
    ram_slots = models.IntegerField(default=4)
    m2_slots = models.IntegerField(default=1)
    image = ImageField()
    offerings = GenericRelation(Offering)

    def __str__(self):
        return '%s. %s - %s' % (self.id, self.name, self.motherboard_form_factor,)


class Memory(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)

    name = models.CharField(max_length=100)
    vendor = models.ForeignKey(Vendor, related_name='memory', to_field='code', on_delete=models.CASCADE)
    modules = models.IntegerField(default=2)
    size = models.IntegerField(default=8)
    frequency = models.IntegerField(default=2400)
    type = models.ForeignKey(MemoryType, related_name='memory', to_field='code', on_delete=models.CASCADE)
    cas = models.IntegerField(default=16)
    image = ImageField()
    offerings = GenericRelation(Offering)

    def __str__(self):
        return '%s. %s - %s' % (self.id, self.type, self.name,)


class GpuVendor(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)

    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=20)
    offerings = GenericRelation(Offering)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

class GpuType(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)

    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    vendor = models.ForeignKey(GpuVendor, related_name='gpu_types', to_field='code', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Gpu(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)

    name = models.CharField(max_length=100)
    vendor = models.ForeignKey(Vendor, related_name='gpus', to_field='code', on_delete=models.CASCADE)
    type = models.ForeignKey(GpuType, related_name='gpus', to_field='code', on_delete=models.CASCADE)
    pcie_six_pin = models.IntegerField()
    pcie_eight_pin = models.IntegerField()
    image = ImageField()
    offerings = GenericRelation(Offering)


    def __str__(self):
        return '%s. %s - %s' % (self.id, self.type, self.name,)


class SsdType(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)

    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('name',)


class Ssd(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)

    name = models.CharField(max_length=100)
    vendor = models.ForeignKey(Vendor, related_name='ssds', to_field='code', on_delete=models.CASCADE)
    type = models.ForeignKey(SsdType, related_name='ssds', to_field='code', on_delete=models.CASCADE)
    capacity = models.IntegerField()
    read_speed = models.IntegerField(null=True, blank=True)
    write_speed = models.IntegerField(null=True, blank=True)
    image = ImageField()
    offerings = GenericRelation(Offering)

    def __str__(self):
        return '%s. %s - %s' % (self.id, self.type, self.name,)


class Hdd(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)

    name = models.CharField(max_length=100)
    vendor = models.ForeignKey(Vendor, related_name='hdds', to_field='code', on_delete=models.CASCADE)
    FORMAT_CHOICES = [
        ('3.5"', '3.5"'),
        ('2.5"', '2.5"'),
    ]
    format = models.CharField(max_length=20, choices=FORMAT_CHOICES, default=FORMAT_CHOICES[0])
    capacity = models.IntegerField()
    image = ImageField()
    offerings = GenericRelation(Offering)

    def __str__(self):
        return '%s. %s - %s' % (self.id, self.format, self.name,)


class Case(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)

    name = models.CharField(max_length=100)
    vendor = models.ForeignKey(Vendor, related_name='cases', to_field='code', on_delete=models.CASCADE)
    motherboard_form_factor = models.ForeignKey(MotherboardFormFactor, related_name='cases', to_field='code', on_delete=models.CASCADE)
    psu_form_factor = models.ForeignKey(PsuFormFactor, related_name='cases', to_field='code', on_delete=models.CASCADE)
    image = ImageField()
    offerings = GenericRelation(Offering)

    def __str__(self):
        return '%s. %s - %s' % (self.id, self.name, self.motherboard_form_factor,)


class Psu(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)

    name = models.CharField(max_length=100)
    vendor = models.ForeignKey(Vendor, related_name='psus', to_field='code', on_delete=models.CASCADE)
    psu_form_factor = models.ForeignKey(PsuFormFactor, related_name='psus', to_field='code', on_delete=models.CASCADE)
    RATING_CHOICES = [
        ('80 Plus', '80 Plus'),
        ('80 Plus Bronze', '80 Plus Bronze'),
        ('80 Plus Silver', '80 Plus Silver'),
        ('80 Plus Gold', '80 Plus Gold'),
        ('80 Plus Platinum', '80 Plus Platinum'),
        ('80 Plus Titanium', '80 Plus Titanium'),
    ]
    rating = models.CharField(max_length=20, choices=RATING_CHOICES, null=True, blank=True)
    watts = models.IntegerField()
    pcie_six_pin = models.IntegerField()
    pcie_eight_pin = models.IntegerField()
    image = ImageField()
    offerings = GenericRelation(Offering)

    def __str__(self):
        return '%s. %s - %sW' % (self.id, self.name, self.watts,)