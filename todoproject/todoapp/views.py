from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm


def index(request):
    todos = Todo.objects.all()

    form = TodoForm()

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'todos': todos, 'form': form}
    return render(request, 'todoapp/home.html', context)


def updateTodo(request, pk):
    todo = Todo.objects.get(id=pk)

    form = TodoForm(instance=todo)

    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'form': form}
    return render(request, 'todoapp/update_todo.html', context)


def deleteTodo(request, pk):
    item = Todo.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item': item}

    return render(request, 'todoapp/delete_todo.html', context)


def deleteAll(request):
    all_items = Todo.objects.all()

    if request.method == 'POST':
        all_items.delete()
        return redirect('/')

    context = {'all_items': all_items}

    return render(request, 'todoapp/deleteall.html', context)