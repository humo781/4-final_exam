from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.views.generic import CreateView
from .forms import RegisterForm

class UserLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = "login.html"

    def form_invalid(self, form):
        print("Form errors:", form.errors)
        return super().form_invalid(form)

def main_page(request):
    return render(request, 'main-page.html')

class RegisterView(CreateView):
    context_object_name = 'form'
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = 'login'

    def form_invalid(self, form):
        print("Form errors:", form.errors)
        return super().form_invalid(form)
