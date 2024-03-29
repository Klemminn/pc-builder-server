# Generated by Django 3.1.2 on 2020-10-13 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offerings', '0008_auto_20201003_2223'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='offering',
            options={'ordering': ('price',)},
        ),
        migrations.AlterModelOptions(
            name='retailer',
            options={'ordering': ('code',)},
        ),
        migrations.AddIndex(
            model_name='offering',
            index=models.Index(fields=['price'], name='offerings_o_price_40e59a_idx'),
        ),
        migrations.AddIndex(
            model_name='offering',
            index=models.Index(fields=['disabled'], name='offerings_o_disable_0e4fc9_idx'),
        ),
    ]
