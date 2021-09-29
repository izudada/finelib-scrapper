from django.http import HttpResponse
from django.urls import  reverse_lazy, reverse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView, CreateView
from .forms import LoginForm, RegisterForm
from .models import User


class IndexView(TemplateView):
    template_name = 'index.html'


class UserCreateView(CreateView):
    model = User
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'

    def form_valid(self, form):
        return super(UserCreateView, self).form_valid(form)