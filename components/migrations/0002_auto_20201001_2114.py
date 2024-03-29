# Generated by Django 3.1.2 on 2020-10-01 21:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CpuCooler',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('fans', models.IntegerField(default=1)),
                ('fan_size', models.IntegerField(default=120)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cpu_coolers', to='components.vendor', to_field='code')),
            ],
        ),
        migrations.CreateModel(
            name='GpuVendor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('code', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='StorageType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('code', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='motherboardchipset',
            old_name='max_memory_speed',
            new_name='max_memory_frequency',
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='storages', to='components.storagetype', to_field='code')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='storages', to='components.vendor', to_field='code')),
            ],
        ),
        migrations.CreateModel(
            name='Memory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('modules', models.IntegerField(default=2)),
                ('frequency', models.IntegerField(default=2400)),
                ('cas', models.IntegerField(default=16)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memory', to='components.memorytype', to_field='code')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memory', to='components.vendor', to_field='code')),
            ],
        ),
        migrations.CreateModel(
            name='GpuType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('code', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gpu_types', to='components.gpuvendor', to_field='code')),
            ],
        ),
        migrations.CreateModel(
            name='Gpu',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gpus', to='components.gputype', to_field='code')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gpus', to='components.vendor', to_field='code')),
            ],
        ),
        migrations.CreateModel(
            name='CpuCoolerSocketConnection',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('cooler', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cpu_cooler_socket_connections', to='components.cpucooler', to_field='name')),
                ('socket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cpu_cooler_socket_connections', to='components.cpusocket', to_field='code')),
            ],
        ),
        migrations.CreateModel(
            name='Cpu',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('cores', models.IntegerField(default=6)),
                ('threads', models.IntegerField(default=6)),
                ('core_clock', models.IntegerField()),
                ('boost_clock', models.IntegerField()),
                ('tdp', models.IntegerField()),
                ('graphics', models.CharField(blank=True, max_length=30, null=True)),
                ('cpu_socket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cpus', to='components.cpusocket', to_field='code')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cpus', to='components.vendor', to_field='code')),
            ],
        ),
    ]
