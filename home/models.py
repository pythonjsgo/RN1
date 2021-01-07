from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.core import blocks
from wagtail.core.fields import StreamField

from wagtail.core.models import Page
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel

from blog.models import BlogDetailPage



from wagtailnews.feeds import LatestEntriesFeed




class HomePage(RoutablePageMixin, Page):

    max_count = 1

    images = StreamField([
        ('image', ImageChooserBlock()),
    ])

    content_panels = Page.content_panels + [
    #    ImageChooserPanel('image'),
        StreamFieldPanel('images')
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["posts"] = BlogDetailPage.objects.live().public()

        return context
"""
    @route(r'^$')
    def new_page(self, request, *arg, **kwargs):
        context = self.get_context(request, *arg, **kwargs)

        pass
        
"""