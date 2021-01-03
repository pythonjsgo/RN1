from django.db import models

# Create your models here.
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index


class BlogPage(Page):
    date = models.DateTimeField("Post date")
    author = models.CharField(max_length=30, null=True)
    preview_image = models.ForeignKey(  'wagtailimages.Image', on_delete=models.CASCADE, related_name='+' , null = True)
    intro = models.CharField(max_length=250)
    body = RichTextField()
    theme = models.CharField(max_length=20)




    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        ImageChooserPanel("preview_image"),
        FieldPanel("author"),
        FieldPanel('date'),
        FieldPanel('theme'),
        FieldPanel('intro'),
        FieldPanel('body', classname="full"),
    ]