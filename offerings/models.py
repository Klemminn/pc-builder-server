from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models


class Retailer(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)

    code = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=30)
    website = models.URLField()

    def __str__(self):
        return self.name


class Offering(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    object_id = models.PositiveIntegerField(null=True)
    content_object = GenericForeignKey('content_type', 'object_id')
    retailer = models.ForeignKey(Retailer, related_name='offerings', to_field='code', on_delete=models.CASCADE)
    price = models.IntegerField()
    url = models.URLField()
    disabled = models.BooleanField(null=True)

