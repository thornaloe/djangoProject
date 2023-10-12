from django.views.generic import ListView, DetailView, TemplateView
from .models import Post

#создаем модель, кот будет отвечать за домашную страницу
class Bloglist(ListView):
    model = Post
    template_name = 'home.html'

#создаем модель, кот будет отвечать за деталь поста
class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class AboutPageView(TemplateView):
    template_name = 'post_detail.html'



