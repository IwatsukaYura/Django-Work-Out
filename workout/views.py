from django.contrib import admin
from django.shortcuts import render
from django.contrib.auth import login
from .forms import SignupForm, LoginForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

#ユーザーアカウントの登録用View
class MySignupView(CreateView):
    template_name = 'workout/signup.html'
    form_class = SignupForm
    success_url = '/workout/user/'

    #form_validのオーバーライドによってデータの保存だけでなく、ログインを実現
    def form_valid(self, form):
        result = super().form_valid(form)
        user = self.object
        login(self.request, user)
        return result
    
#ログイン用のView
class MyLoginView(LoginView):
    template_name = 'workout/login.html'
    form_class = LoginForm
#ログアウト用のView
class MyLogoutView(LogoutView):
    template_name = 'workout/logout.html'
    
#LoginRequiredMixinで未ログインユーザからのアクセスを禁止している。
class MyUserView(LoginRequiredMixin, TemplateView):
    template_name = 'workout/user.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
    
class MyOtherView(LoginRequiredMixin, TemplateView):
    template_name = 'workout/other.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = CustomUser.objects.exclude(username=self.request.user.username)
        return context
