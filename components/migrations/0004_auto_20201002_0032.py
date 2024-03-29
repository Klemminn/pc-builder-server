# Generated by Django 3.1.2 on 2020-10-02 00:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0003_auto_20201001_2135'),
    ]

    operations = [
        migrations.AddField(
            model_name='gpu',
            name='pcie_eight_pin',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gpu',
            name='pcie_six_pin',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Psu',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('watts', models.IntegerField()),
                ('pcie_six_pin', models.IntegerField()),
                ('pcie_eight_pin', models.IntegerField()),
                ('psu_form_factor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='psus', to='components.psuformfactor', to_field='code')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='psus', to='components.vendor', to_field='code')),
            ],
        ),
    ]
