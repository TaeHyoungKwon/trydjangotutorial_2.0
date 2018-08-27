from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from .forms import ArticleModelForm
from .models import Article


class ArticleCreateView(CreateView):
    template_name = 'blog/article_create.html'
    form_class = ArticleModelForm

    def form_valid(self, form):
        print(form.cleaned_data)
        print(super())
        return super().form_valid(form)



class ArticleListView(ListView):
    template_name = 'blog/article_list.html'
    queryset = Article.objects.all()



class ArticleDetailView(DetailView):
    template_name = 'blog/article_detail.html'

    def get_object(self):
        id_ = self.kwargs.get("my_id")
        return get_object_or_404(Article, id=id_)



class ArticleUpdateView(UpdateView):
    template_name = 'blog/article_create.html'
    form_class = ArticleModelForm

    def get_object(self):
        id_ = self.kwargs.get("my_id")
        return get_object_or_404(Article, id=id_)
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class ArticleDeleteView(DeleteView):
    template_name = 'blog/article_delete.html'
    #success_url = "/blog"

    def get_object(self):
        id_ = self.kwargs.get("my_id")
        return get_object_or_404(Article, id=id_)

    def get_success_url(self):
        return reverse('articles:article-list')
    
