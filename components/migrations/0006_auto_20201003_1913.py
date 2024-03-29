# Generated by Django 3.1.2 on 2020-10-03 19:13

import builder.utils
import builder.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0005_delete_cpucoolersocketconnection'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=builder.utils.handle_upload, validators=[builder.validators.validate_image_extension]),
        ),
        migrations.AddField(
            model_name='cpu',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=builder.utils.handle_upload, validators=[builder.validators.validate_image_extension]),
        ),
        migrations.AddField(
            model_name='cpucooler',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=builder.utils.handle_upload, validators=[builder.validators.validate_image_extension]),
        ),
        migrations.AddField(
            model_name='gpu',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=builder.utils.handle_upload, validators=[builder.validators.validate_image_extension]),
        ),
        migrations.AddField(
            model_name='memory',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=builder.utils.handle_upload, validators=[builder.validators.validate_image_extension]),
        ),
        migrations.AddField(
            model_name='motherboard',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=builder.utils.handle_upload, validators=[builder.validators.validate_image_extension]),
        ),
        migrations.AddField(
            model_name='psu',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=builder.utils.handle_upload, validators=[builder.validators.validate_image_extension]),
        ),
        migrations.AddField(
            model_name='storage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=builder.utils.handle_upload, validators=[builder.validators.validate_image_extension]),
        ),
    ]
