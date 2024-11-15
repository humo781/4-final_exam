from django.urls import path
from .views import login_view, RegisterView

urlpatterns = [
    path('', RegisterView.as_view(), name='register'),
    path('login/', login_view, name='login'),
]
