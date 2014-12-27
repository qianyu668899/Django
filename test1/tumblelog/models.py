from django.db import models

# Create your models here.
from django.contrib.contenttypes import generic

from django.db.models import signals
from django.contrib.contenttypes.models import ContentType
from django.dispatch import dispatcher
from blog.models import Entry
from links.models import Link

class TumbleItem(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    pub_date = models.DateTimeField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    class Meta:
        ordering = ('-pub_date',)

    def __unicode__(self):
        return self.content_type.name

	def __getContent(self):
		return '%s %s' %(self.content_type, self.content_object)
	content = property(__getContent)
		




