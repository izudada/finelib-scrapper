from django.http import HttpResponse
from django.urls import  reverse_lazy, reverse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView
from account.models import User


class Dashboard(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'