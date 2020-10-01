from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models
import uuid

CODE_LENGTH = 5

class Build(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)

    code = models.CharField(max_length=CODE_LENGTH, unique=True)

    def __str__(self):
        return self.code

    def save(self, *args, **kwargs):
        if len(self.code) == 0:
            while True:
                code = uuid.uuid4().hex[:CODE_LENGTH].upper()
                if not Build.objects.filter(code=code).exists():
                    break
            self.code = code
        super(Build, self).save(*args, **kwargs)


class Component(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)

    build = models.ForeignKey(Build, related_name='components', to_field='code', on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
