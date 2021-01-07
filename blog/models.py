from django.db import models

# Create your models here.

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from wagtailnews.feeds import LatestEntriesFeed
from wagtailnews.models import NewsIndexMixin

class MyNewsFeed(LatestEntriesFeed):
    def item_description(self, item):
        return item.description





class BlogListingPage(Page):

    max_count = 1

    custom_title = models.CharField(max_length=100, blank=True, null=True)

    @property
    def get_child_pages(self):
        return self.get_children().public().live()
        # return self.get_children().public().live().values("id", "title", "slug")


    def get_context(self, request, *args, **kwargs):
        """Adding custom stuff to our context."""
        context = super().get_context(request, *args, **kwargs)
        # Get all posts
        all_posts = BlogDetailPage.objects.live().public().order_by('-first_published_at')
        # Paginate all posts by 2 per page
        paginator = Paginator(all_posts, 5)
        # Try to get the ?page=x value
        page = request.GET.get("page")
        print(page)
        try:
            # If the page exists and the ?page=x is an int
            posts = paginator.page(page)
            print(posts)
        except PageNotAnInteger:
            # If the ?page=x is not an int; show the first page
            posts = paginator.page(1)
        except EmptyPage:
            # If the ?page=x is out of range (too high most likely)
            # Then return the last page
            posts = paginator.page(paginator.num_pages)

        # "posts" will have child pages; you'll need to use .specific in the template
        # in order to access child properties, such as youtube_video_id and subtitle
        context["posts"] = posts
        print(type(posts))
        return context



class BlogDetailPage( Page):

    template = "blog/blog_page.html"
    feed_class = MyNewsFeed

    date = models.DateTimeField("Post date")
    author = models.CharField(max_length=30, null=True)
    preview_image = models.ForeignKey(  'wagtailimages.Image', on_delete=models.CASCADE, related_name='+' , null = True)
    intro = models.CharField(max_length=250)
    body = RichTextField()
    theme = models.CharField(max_length=20)





    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
        index.SearchField('title'),
    ]

    content_panels = Page.content_panels + [
        ImageChooserPanel("preview_image"),
        FieldPanel("author"),
        FieldPanel('date'),
        FieldPanel('theme'),
        FieldPanel('intro'),
        FieldPanel('body', classname="full"),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["posts"] = BlogDetailPage.objects.live().public()

        return context

