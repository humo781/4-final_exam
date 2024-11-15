from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import RegisterForm

def login_view(request):
    return render(request, 'login.html')

class RegisterView(CreateView):
    context_object_name = 'form'
    template_name = 'register.html'
    form_class = RegisterForm

    def form_invalid(self, form):
        print("Form errors:", form.errors)
        return super().form_invalid(form)
