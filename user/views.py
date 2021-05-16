from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.views.generic import FormView
from .models import User
from django.contrib.auth.hashers import make_password
# Create your views here.

def home(request):
    return render(request, '../templates/user/home.html')

class LoginView(FormView):
    template_name = 'user/login.html'
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):
        self.request.session['user'] = form.data.get('userid')

        return super().form_valid(form)

def logout(request):
    if request.session.get('user'): #로그인 되어있을때
        del(request.session['user'])#로그인한 정보

    return redirect('/')



class RegisterView(FormView):
    template_name = 'user/register.html'
    form_class = RegisterForm
    success_url = '../login'
    def form_valid(self, form):
        user = User(
            userid=form.data.get('userid'),
            password=make_password(form.data.get('password')),
            nickname=form.data.get('nickname')
        )
        user.save()
        return super().form_valid(form)