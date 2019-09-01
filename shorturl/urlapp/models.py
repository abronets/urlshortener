from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Url(models.Model):
    short_id = models.SlugField(max_length=6, primary_key=True, blank=True)
    short_url = models.URLField(max_length=250)
    long_url = models.URLField(max_length=250)

    def __str__(self):
        return 'Url : {} Short_id : {}'.format(self.long_url, self.short_id)

    class Meta:
        verbose_name = _('Url')
        verbose_name_plural = _('Urls')