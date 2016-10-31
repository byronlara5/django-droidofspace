import os
from django.db import models
from django.db.models import permalink
from django.template.defaultfilters import slugify
from django.utils import timezone



from zinnia.settings import UPLOAD_TO_GALLERY

from django.utils.translation import ugettext_lazy as _

from zinnia.models.entry import Entry

# Create your models here.


def photo_upload_to_dispatcher(entry, filename):
    """
    Dispatch function to allow overriding of ``image_upload_to`` method.
    Outside the model for fixing an issue with Django's migrations on Python 2.
    """
    return entry.photo_upload_to(filename)

class Photo(models.Model):

	def photo_upload_to(self, filename):

		now = timezone.now()
		filename, extension = os.path.splitext(filename)

		return os.path.join(
			UPLOAD_TO_GALLERY,
			now.strftime('%Y'),
			now.strftime('%m'),
			now.strftime('%d'),
			'%s%s' % (slugify(filename), extension))

	src = models.ImageField(upload_to=photo_upload_to_dispatcher,
									help_text=_('Used for gallery'))
	credit = models.CharField(max_length=50,null=True,blank=True)




class EntryPhoto(models.Model):
	entry = models.ForeignKey(Entry,verbose_name=_('entry'))
	photo = models.ForeignKey(Photo)