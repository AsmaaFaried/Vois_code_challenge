from django.db import models
from django.utils.translation import gettext_lazy as _
import os


def _get_file_path(instance, filename):
    """Generate File Path"""
    file_path = os.path.join('attachments/', filename)
    return file_path


class Attachment(models.Model):
    file = models.FileField(upload_to=_get_file_path, null=True, blank=True, verbose_name=_('File'))
    uploaded_on = models.DateTimeField(auto_now_add=True, verbose_name=_('Uploaded on'))

    class Meta:
        verbose_name = _("Attachment")
        verbose_name_plural = _("Attachments")
        ordering = ('-uploaded_on',)

    def __str__(self):

        return self.uploaded_on
