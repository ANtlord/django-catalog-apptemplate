from django.db import models
from django.core.urlresolvers import reverse

class Instance(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(max_length=255)
    text = models.TextField(max_length=2047, blank=True, null=True)
    short_text = models.CharField(max_length=255, blank=True)

    def __unicode__(self):
        return self.name


class Section(Instance):
    """Model of Section"""
    class Meta:
        verbose_name = u'section'
        verbose_name_plural = u'sections'

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('item-list', kwargs={'section_id': self.pk})


class Item(Instance):
    """Model of item"""
    class Meta:
        verbose_name = u'item'
        verbose_name_plural = u'items'
    
    section = models.ForeignKey(Section, related_name='items')

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('item-detail', kwargs={'pk': self.pk})
