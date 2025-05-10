from django.shortcuts import render, HttpResponse, redirect
from .models import TodoItem
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import MyForm


# Create your views here.
def todos(request):
    items = TodoItem.objects.all()
    return render(request, 'todos.html', {'todos': items})


def create(request):
    form = MyForm(request.POST)

    if form.is_valid():
        form.save()
        return redirect(request, 'todos')
    else:
        form = MyForm()
    return render(request, 'todos.html', {'form': form})




