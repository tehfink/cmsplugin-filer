from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from django.utils.translation import ugettext_lazy as _
from cmsplugin_filer_image import models
from django.conf import settings

class FilerImagePlugin(CMSPluginBase):
    model = models.FilerImage
    name = _("Image (Filer)")

    render_template_base = "cmsplugin_filer_image"
    text_enabled = True
    raw_id_fields = ('image',)

    def render(self, context, instance, placeholder):

        try:
            template = settings.CMS_PLACEHOLDER_CONF[instance.placeholder]['extra_context'][self.__class__.__name__]['render_template']
        except (KeyError, AttributeError):
            template = "image.html"

        import os
        self.render_template = os.path.join(self.render_template_base, template)

        # TODO: this scaling code needs to be in a common place
        # use the placeholder width as a hint for sizing
        placeholder_width = context.get('width', None)
        if instance.use_autoscale and placeholder_width:
            width = placeholder_width
        else:
            if instance.width:
                width = instance.width
            else:
                width = instance.image.width
        if instance.height:
            height = instance.height
            if width == instance.image.width:
                # width was not externally defined: use ratio to scale it by the height
                width = int( float(height)*float(instance.image.width)/float(instance.image.height) )
        else:
            # height was not externally defined: use ratio to scale it by the width
            height = int( float(width)*float(instance.image.height)/float(instance.image.width) )

        context.update({
            'object':instance,
            'link':instance.link,
            #'image_url':instance.scaled_image_url,
            'image_size': u'%sx%s' % (width, height),
            'image_width': width,
            'image_height': height,
            'placeholder':placeholder
        })
        return context
    def icon_src(self, instance):
        return instance.image.thumbnails['admin_tiny_icon']
plugin_pool.register_plugin(FilerImagePlugin)
