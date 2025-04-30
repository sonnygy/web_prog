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

from django.views.decorators.csrf import csrf_protect

@csrf_protect
def sign_up_view(request):
    form = ApplicationForm(request.POST if request.method == 'POST' else None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Заявка отправлена!')
        return redirect(reverse('sign-up') + '?success=1')
    elif request.method == 'POST':
        messages.error(request, 'Проверьте правильность заполнения формы.')
    return render(request, 'myapp/sign-up.html', {'form': form})
def success(request):
  return render(request, 'myapp/sign-up.html')
