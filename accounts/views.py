from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


# 汎用ビューのCreateViewを継承したSignUpViewクラスを作成
class SignUpView(generic.CreateView):
    form_class = UserCreationForm           # フォームクラスを指定
    success_url = reverse_lazy('login')     # サインアップ成功時のリダイレクト先
    template_name = 'accounts/signup.html'  # テンプレートファイルを指定