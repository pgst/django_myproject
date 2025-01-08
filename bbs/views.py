from django.views import generic
from .models import Article
from django.urls import reverse_lazy
from django.shortcuts import render
from .forms import SearchForm  # forms.pyからSearchFormをインポート
# ログインしていないユーザーをリダイレクトするためにインポート
from django.contrib.auth.mixins import LoginRequiredMixin
# ログインしていないユーザーに対して403エラーを返すためにインポート
from django.core.exceptions import PermissionDenied


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
class CreateView(LoginRequiredMixin, generic.edit.CreateView):
    model = Article
    template_name = 'bbs/create.html'
    fields = '__all__'


# UpdateViewクラスを作成
class UpdateView(LoginRequiredMixin, generic.edit.UpdateView):
    model = Article
    template_name = 'bbs/create.html'
    fields = ['content']

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied('編集権限がありません')
        return super(UpdateView, self).dispatch(request, *args, **kwargs)


# DeleteViewクラスを作成
class DeleteView(LoginRequiredMixin, generic.edit.DeleteView):
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
        return render(request, 'bbs/results.html',
                      {'articles': articles, 'searchform': searchform})