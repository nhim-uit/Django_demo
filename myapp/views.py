from .models import TodoItem
from django.shortcuts import render, redirect, get_object_or_404
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
        return redirect('todos')
    else:
        form = MyForm()
    return render(request, 'todos.html', {'form': form})


def edit(request, id):
    todo = get_object_or_404(TodoItem, id=id)
    form = MyForm(request.POST)

    if form.is_valid():
        if 'title' in request.POST:
            title = request.POST['title']
        if 'completed' in request.POST:
            completed = request.POST['completed']
        else:
            completed = False

        todo.title = title
        todo.completed = completed
        todo.save()
        return redirect('todos')

    return render(request, 'edit.html', {'form': form, 'todos': todo})


def delete(request, id):
    todo = get_object_or_404(TodoItem, id=id)
    todo.delete()
    return render(request, 'todos.html', {'todos': TodoItem.objects.all()})