from django.contrib.syndication.views import Feed
from blog.models import BlogDetailPage
from django.utils.feedgenerator import Atom1Feed


class RssFeed(Feed):
    title = "новости RusNews"
    link = "/"
    description = "A blog about cyber security, web development and other tech related topics"
    feed_url = '/rss/'
    author_name = 'RusNews'
    categories = ("RusNews", "политика", "протесты", "новости россии", "митинги")
    feed_copyright = 'Copyright (c) 2020-2021, RusNews'

    language = 'ru'

    def items(self):
        return BlogDetailPage.objects.order_by('-date')[:5]

    def item_title(self, item):
        return item.title

    # return a short description of article
    def item_description(self, item):
        return item.intro

    # return the URL of the article
    def item_link(self, item):
        return item.full_url

    # return the date the article was published
    def item_pubdate(self, item):
        return item.first_published_at

    # return the date of the last update of the article
    def item_updateddate(self, item):
        return item.last_published_at

    # return the categories of the article


class AtomFeed(RssFeed):
    feed_type = Atom1Feed
    link = "/atom/"
    subtitle = RssFeed.description