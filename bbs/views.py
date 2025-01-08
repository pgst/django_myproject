from django.views import generic
from .models import Article
from django.urls import reverse_lazy
from django.shortcuts import render
from .forms import SearchForm  # forms.pyからSearchFormをインポート


# IndexViewクラスを作成
class IndexView(generic.ListView):
    # モデルの指定
    model = Article
    # テンプレートファイルの指定
    template_name = 'bbs/index.html'

# DetailViewクラスを作成
class DetailView(generic.DetailView):
    model = Article
    template_name = 'bbs/detail.html'


# CreateViewクラスを作成
class CreateView(generic.CreateView):
    model = Article
    template_name = 'bbs/create.html'
    fields = '__all__'


# UpdateViewクラスを作成
class UpdateView(generic.UpdateView):
    model = Article
    template_name = 'bbs/create.html'
    fields = '__all__'


# DeleteViewクラスを作成
class DeleteView(generic.edit.DeleteView):
    model = Article
    template_name = 'bbs/delete.html'
    success_url = reverse_lazy('bbs:index')


# search関数を作成
def search(request):
    articles = None
    searchform = SearchForm(request.GET)

    # Formに正常なデータがあれば
    if searchform.is_valid():
        # queryにフォームが持っているクエリを代入
        query = searchform.cleaned_data['query']
        # クエリを含むレコードをfilterメソッドで取り出し、articlesに代入
        articles = Article.objects.filter(content__icontains=query)
        return render(request, 'bbs/results.html', {'articles': articles, 'searchform': searchform})