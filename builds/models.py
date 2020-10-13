from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models
import uuid

CODE_LENGTH = 5

class Build(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)

    code = models.CharField(max_length=CODE_LENGTH, unique=True)
    offerings = models.JSONField(unique=True)

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
