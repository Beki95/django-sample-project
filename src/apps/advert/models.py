from application.models import BaseModel
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Advert(BaseModel):
    title = models.CharField(
        verbose_name=_('Title'),
        max_length=255,
    )
    description = models.TextField(
        verbose_name=_('Description')
    )
    city = models.ForeignKey(
        verbose_name=_('City'),
        to='city.City',
        on_delete=models.CASCADE,
        related_name='adverts',
    )
    category = models.ForeignKey(
        verbose_name=_('Category'),
        to='category.Category',
        on_delete=models.CASCADE,
        related_name='adverts',
    )
    views = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = _('Advert')
        verbose_name_plural = _('Adverts')

    def __str__(self):
        return self.title
