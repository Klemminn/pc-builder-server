from django.db import models


class MotherboardFormFactor(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)

    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class PsuFormFactor(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)

    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class MemoryType(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)

    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name


class CpuSocket(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)

    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=10)

    def __str__(self):
        return '%s - %s' % (self.code, self.name,)


class Vendor(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)

    code = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    

class MotherboardChipset(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)

    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=10)
    max_memory_frequency = models.IntegerField()
    memory_type = models.ForeignKey(MemoryType, related_name='motherboard_chipsets', to_field='code', on_delete=models.CASCADE)
    cpu_socket = models.ForeignKey(CpuSocket, related_name='motherboard_chipsets', to_field='code', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Case(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)

    name = models.CharField(max_length=100)
    vendor = models.ForeignKey(Vendor, related_name='cases', to_field='code', on_delete=models.CASCADE)
    motherboard_form_factor = models.ForeignKey(MotherboardFormFactor, related_name='cases', to_field='code', on_delete=models.CASCADE)
    psu_form_factor = models.ForeignKey(PsuFormFactor, related_name='cases', to_field='code', on_delete=models.CASCADE)

    def __str__(self):
        return '%s - %s' % (self.name, self.motherboard_form_factor,)


class Motherboard(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)

    name = models.CharField(max_length=100)
    vendor = models.ForeignKey(Vendor, related_name='motherboards', to_field='code', on_delete=models.CASCADE)
    motherboard_form_factor = models.ForeignKey(MotherboardFormFactor, related_name='motherboards', to_field='code', on_delete=models.CASCADE)
    chipset = models.ForeignKey(MotherboardChipset, related_name='motherboards', to_field='code', on_delete=models.CASCADE)
    ram_slots = models.IntegerField(default=4)
    m2_slots = models.IntegerField(default=1)

    def __str__(self):
        return '%s - %s' % (self.name, self.motherboard_form_factor,)


class Cpu(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)

    name = models.CharField(max_length=100)
    vendor = models.ForeignKey(Vendor, related_name='cpus', to_field='code', on_delete=models.CASCADE)
    cpu_socket = models.ForeignKey(CpuSocket, related_name='cpus', to_field='code', on_delete=models.CASCADE)
    cores = models.IntegerField(default=6)
    threads = models.IntegerField(default=6)
    core_clock = models.IntegerField()
    boost_clock = models.IntegerField()
    tdp = models.IntegerField()
    graphics = models.CharField(null=True, blank=True, max_length=30)

    def __str__(self):
        return '%s - %s' % (self.cpu_socket, self.name,)


class CpuCooler(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)

    name = models.CharField(max_length=100, unique=True)
    vendor = models.ForeignKey(Vendor, related_name='cpu_coolers', to_field='code', on_delete=models.CASCADE)
    fans = models.IntegerField(default=1)
    fan_size = models.IntegerField(default=120)


class CpuCoolerSocketConnection(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)

    socket = models.ForeignKey(CpuSocket, related_name='cpu_cooler_socket_connections', to_field='code', on_delete=models.CASCADE)
    cooler = models.ForeignKey(CpuCooler, related_name='cpu_cooler_socket_connections', to_field='name', on_delete=models.CASCADE)


class Memory(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)

    name = models.CharField(max_length=100)
    vendor = models.ForeignKey(Vendor, related_name='memory', to_field='code', on_delete=models.CASCADE)
    modules = models.IntegerField(default=2)
    frequency = models.IntegerField(default=2400)
    type = models.ForeignKey(MemoryType, related_name='memory', to_field='code', on_delete=models.CASCADE)
    cas = models.IntegerField(default=16)

    def __str__(self):
        return '%s - %s' % (self.type, self.name,)


class GpuVendor(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)

    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class GpuType(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)

    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    vendor = models.ForeignKey(GpuVendor, related_name='gpu_types', to_field='code', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


class Gpu(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)

    name = models.CharField(max_length=100)
    vendor = models.ForeignKey(Vendor, related_name='gpus', to_field='code', on_delete=models.CASCADE)
    type = models.ForeignKey(GpuType, related_name='gpus', to_field='code', on_delete=models.CASCADE)
    memory = models.IntegerField()
    core_clock = models.IntegerField()
    boost_clock = models.IntegerField()
    tdp = models.IntegerField()


    def __str__(self):
        return '%s - %s' % (self.type, self.name,)


class StorageType(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)

    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Storage(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)

    name = models.CharField(max_length=100)
    vendor = models.ForeignKey(Vendor, related_name='storages', to_field='code', on_delete=models.CASCADE)
    type = models.ForeignKey(StorageType, related_name='storages', to_field='code', on_delete=models.CASCADE)
    capacity = models.IntegerField()
    read_speed = models.IntegerField()
    write_speed = models.IntegerField()

    def __str__(self):
        return '%s - %s' % (self.type, self.name,)