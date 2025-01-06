from django.views import generic
from .models import Article


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