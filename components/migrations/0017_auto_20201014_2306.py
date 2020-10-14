# Generated by Django 3.1.2 on 2020-10-14 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0016_psu_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='psu',
            name='rating',
            field=models.CharField(choices=[('none', None), ('white', '80 Plus'), ('bronze', '80 Plus Bronze'), ('silver', '80 Plus Silver'), ('gold', '80 Plus Gold'), ('platinum', '80 Plus Platinum'), ('titanium', '80 Plus Titanium')], default=('none', None), max_length=20),
        ),
    ]