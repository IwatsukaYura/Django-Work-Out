from django.contrib import admin
from django.shortcuts import render
from django.contrib.auth import login
from .forms import SignupForm, LoginForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

CustomUser = get_user_model()

#ユーザーアカウントの登録用View
class MySignupView(CreateView):
    template_name = 'workout/signup.html'
    form_class = SignupForm
    success_url = '/workout/user/'

    #form_validのオーバーライドによってデータの保存だけでなく、ログインを実現
    #フォームデータが妥当であるときのみ実行される
    def form_valid(self, form):
        result = super().form_valid(form)   #データをレコードに保存
        user = self.object
        print(form)
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
    login_url = '/workout/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
    
# class MyOtherView(LoginRequiredMixin, TemplateView):
#     template_name = 'workout/other.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['users'] = CustomUser.objects.exclude(username=self.request.user.username)
#         return context

class UserWightChangeView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    fields = ('weight',)
    template_name = 'workout/recordweight.html'
    success_url = '/workout/changeweight/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = CustomUser.objects.exclude(username=self.request.user.username)
        return context

    def get_object(self):
        return self.request.user
    
class ChoiceTrainingView(LoginRequiredMixin, TemplateView):
    template_name = 'workout/choicetraining.html'
    pass

class ChoiceRecordView(LoginRequiredMixin, TemplateView):
    template_name = 'workout/choicerecord.html'
    pass