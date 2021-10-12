from django.shortcuts import render, redirect
from .models import Article
from .forms import Articleform
from django.views.generic import DetailView, UpdateView, DeleteView
somenews = Article.objects.all()
def MyNews(request):
    return render(request, "news/news.html", {'mynews': somenews})
def CreateNews(request):
    if request.method == "POST":
        form = Articleform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')

    form = Articleform
    data = {"form": form}
    return render(request, "news/create.html", data)
class news_detail_views(DetailView):
    model = Article
    template_name = 'news/detailview.html'
    context_object_name = 'article'

class news_update_views(UpdateView):
    model = Article
    template_name = 'news/create.html'
    form_class = Articleform
    context_object_name = 'article'

class news_delete_views(DeleteView):
    model = Article
    template_name = 'news/delete.html'
    form_class = Articleform
    context_object_name = 'article'
    success_url = "main"
# Create your views here.
