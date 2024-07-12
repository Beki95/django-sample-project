from application.models import BaseModel
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class City(BaseModel):
    name = models.CharField(
        verbose_name=_('Name'),
        max_length=32,
        unique=True,
    )

    class Meta:
        verbose_name = _('City')
        verbose_name_plural = _('Cities')

    def __str__(self): return self.name
