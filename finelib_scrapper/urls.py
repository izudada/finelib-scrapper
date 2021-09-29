from django.urls import include, path
from . import views 

urlpatterns = [
    path('dashboard/', views.Dashboard.as_view(), name='dashboard'),
]