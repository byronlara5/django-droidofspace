from __future__ import unicode_literals

import os
from django.db import models
from django.db.models import permalink
from django.template.defaultfilters import slugify
from django.utils import timezone

from django.utils.translation import ugettext_lazy as _



# Create your models here.

class Ads(models.Model):

	title = models.CharField(max_length=50, null=False, blank=False, default='none')

	src = models.ImageField(upload_to='uploads/publi',
									help_text=_('Tamano recomendado: 640x640'))
	link = models.CharField(max_length=50,null=True,blank=True)

	index = models.BooleanField(
        _('index'), default=False)

	article = models.BooleanField(
        _('article'), default=False)

	def __unicode__(self):
		return self.title