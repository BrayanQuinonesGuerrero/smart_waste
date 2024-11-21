from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home/index.html'


class ContactView(TemplateView):
    template_name = 'home/contact.html'