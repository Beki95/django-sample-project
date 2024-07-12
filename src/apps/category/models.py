from application.models import BaseModel
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Category(BaseModel):
    name = models.CharField(
        verbose_name=_('Name'),
        max_length=255,
        unique=True,
    )

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self): return self.name
