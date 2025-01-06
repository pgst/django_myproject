from django.contrib import admin
from .models import Article  # models.pyからArticleモデルをインポート


admin.site.register(Article)  # 管理画面にArticleモデルを登錫