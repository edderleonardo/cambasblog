from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, FormView


class Index(TemplateView):
    template_name = 'login.html'


class Posts(TemplateView):
    template_name = 'index/index.html'


class DetailPost(TemplateView):
    template_name = 'index/post-detail.html'
