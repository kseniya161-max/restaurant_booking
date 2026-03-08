from django.shortcuts import redirect
from django.views.generic import TemplateView

from pages.forms import ContactForm


class HomePageView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = ContactForm()
        return context

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('pages:home')

        context = self.get_context_data()
        context["form"] = form
        return self.render_to_response(context)


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'
