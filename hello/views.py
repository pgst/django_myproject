from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Article  # Articleモデルをインポート


def index(request):
    # return HttpResponse("Hello, world!")
    # return render(request, 'hello/index.html')

    articles = Article.objects.all()  # Articleモデルの全レコードを取得
    # article = Article.objects.get(content='チャオ')  # Articleモデルのcontentが「チャオ」のレコードを取得
    # article = Article.objects.get(pk=1)  # ArticleモデルのIDが1のレコードを取得
    # article = Article.objects.first()  # Articleモデルの最初のレコードを取得
    # article = Article.objects.last()  # Articleモデルの最後のレコードを取得
    # articles = []  # 配列articlesを定義
    # articles.append(article)  # 配列articlesにarticleを追加
    # articles = Article.objects.filter(content='こんにちは')
    context = {'articles': articles}  # テンプレートに渡すデータ
    return render(request, 'hello/index.html', context)  # テンプレートをレンダリング

class IndexView(generic.ListView):
    model = Article
    template_name = 'hello/index.html'  # テンプレートファイルの指定