from django.db import models

# Create your models here.
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting

@register_setting
class SocialMediaSettings(BaseSetting):

    facebook = models.CharField(blank=True , null=True, max_length=100 )
    twitter = models.CharField(blank=True , null=True, max_length=100)
    youtube = models.CharField(blank=True , null=True, max_length=100 )
    ok = models.CharField(blank=True, null=True, max_length=100)
    vk = models.CharField(blank=True, null=True, max_length=100)
    dzen = models.CharField(blank=True, null=True, max_length=100)
    telegram = models.CharField(blank=True, null=True, max_length=100)
    instagram = models.CharField(blank=True, null=True, max_length=100)




    panels = [
        MultiFieldPanel([
            FieldPanel("vk"),
            FieldPanel("facebook"),
            FieldPanel("ok"),
            FieldPanel("youtube"),
            FieldPanel("dzen"),
            FieldPanel("twitter"),
            FieldPanel("telegram"),
            FieldPanel("instagram"),
        ], heading="Social Media Setting")
    ]