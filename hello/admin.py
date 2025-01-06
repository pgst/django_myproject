from django.contrib import admin
from .models import Article  # Articleモデルをインポート


admin.site.register(Article)  # Articleモデルを管理サイトに登録
