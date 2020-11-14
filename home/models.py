from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core import blocks
from wagtail.core.fields import StreamField

from wagtail.core.models import Page
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel


class HomePage(Page):

    images =  StreamField([
        ('image', ImageChooserBlock()),
    ])

    content_panels = Page.content_panels + [
    #    ImageChooserPanel('image'),
        StreamFieldPanel('images')
    ]
