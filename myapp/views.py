from django.shortcuts import render, redirect
from .forms import ApplicationForm
from django.urls import reverse
from django.contrib import messages

def home(request):
  return render(request, 'myapp/index.html')
def service(request):
  return render(request, 'myapp/service.html')
def contacts(request):
  return render(request, 'myapp/contact.html')
def sign_up(request):
  return render(request, 'myapp/sign-up.html')

def sign_up_view(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Заявка отправлена!')
            return redirect(reverse('sign-up') + '?success=1')
        else:
            messages.error(request, 'Проверьте правильность заполнения формы.')
    else:
        form = ApplicationForm()
    return render(request, 'myapp/sign-up.html', {'form': form})
def success(request):
  return render(request, 'myapp/sign-up.html')
