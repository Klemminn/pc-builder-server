# Generated by Django 3.1.2 on 2021-05-23 22:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0022_auto_20201019_2210'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='motherboardchipset',
            options={'ordering': ('code',)},
        ),
        migrations.AlterModelOptions(
            name='vendor',
            options={'ordering': ('code',)},
        ),
    ]
