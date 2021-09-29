from django.urls import include, path
from . import views 

urlpatterns = [
    path('account/register/', views.UserCreateView.as_view(), name='register'),
    path('',  views.IndexView.as_view(), name='index' ),
    path('account/', include('django.contrib.auth.urls')),
]