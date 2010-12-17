from django.utils.translation import ugettext_lazy as _
from django.db import models
from cms.models import CMSPlugin, Page
from cms.models.fields import PageField
from sorl.thumbnail.main import DjangoThumbnail
from django.utils.translation import ugettext_lazy as _
from posixpath import join, basename, splitext, exists
from filer.fields.image import FilerImageField
from filer.fields.file import FilerFileField
from cms import settings as cms_settings
from django.conf import settings

CMSPLUGIN_FILER_TEASER_STYLE_CHOICES = getattr( settings, 'CMSPLUGIN_FILER_TEASER_STYLE_CHOICES',() )

class FilerTeaser(CMSPlugin):
    """
    A Teaser
    """
    title = models.CharField(_("title"), max_length=255)
    image = FilerImageField(blank=True, null=True)
    image_url = models.URLField(_("alternative image url"), verify_exists=False, null=True, blank=True, default=None)
    
    style = models.CharField(_("teaser style"), max_length=255, null=True, blank=True, choices=CMSPLUGIN_FILER_TEASER_STYLE_CHOICES)
    
    use_autoscale = models.BooleanField(_("use automatic scaling"), default=True, 
                                        help_text=_('tries to auto scale the image based on the placeholder context'))
    width = models.PositiveIntegerField(null=True, blank=True)
    height = models.PositiveIntegerField(null=True, blank=True)
    
    free_link = models.CharField(_("link"), max_length=255, blank=True, null=True, help_text=_("if present image will be clickable"))
    page_link = PageField(verbose_name=_("page"), null=True, blank=True, help_text=_("if present image will be clickable"))
    description = models.TextField(_("description"), blank=True, null=True)
    
    target_blank = models.BooleanField(_("open link in new window"), default=False)
    
    def __unicode__(self):
        return self.title

    @property
    def link(self):
        try:
            if self.free_link:
                return self.free_link
            elif self.page_link and self.page_link:
                return self.page_link.get_absolute_url()
            else:
                return ''
        except Exception, e:
            print e