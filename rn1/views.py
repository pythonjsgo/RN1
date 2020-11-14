from django.views.generic import TemplateView

class AboutPageView(TemplateView):
    template_name = 'about.html'


class ContactsPageView(TemplateView):
    template_name = 'contacts.html'


class ArticlesPageView(TemplateView):
    template_name = 'articles.html'