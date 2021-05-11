from django.urls import path
from . import views
from .views import RegisterView

urlpatterns = [
    path('login/', views.login),
    path('logout/', views.logout),
    path('register/', RegisterView.as_view())
]