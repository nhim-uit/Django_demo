from django.http import HttpResponse

from .models import TodoItem
from django.shortcuts import render, redirect
from .forms import MyForm


# Create your views here.
def todos(request):
    items = TodoItem.objects.all()
    return render(request, 'todos.html', {'todos': items})


def create_todo(request):
    form = MyForm(request.POST)
    print(form.errors.as_data())
    if form.is_valid():
        if 'title' in request.POST:
            title = request.POST['title']
        if 'completed' in request.POST:
            completed = request.POST['completed']
        else:
            completed = False
        todo = TodoItem.objects.create(title=title, completed=completed)
        todo.save()
        return redirect( 'todos')
    else:
        print('yes')
        form = MyForm()
    return render(request, 'todos.html', {'form': form})
