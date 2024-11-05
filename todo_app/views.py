from django.http import JsonResponse
from .llm import get_cohere_response
from .models import Todo
from django.shortcuts import get_object_or_404, render, redirect
from .forms import TodoForm

def todo_view(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False) 
           
            todo.llm_response = get_cohere_response(todo.title) 
            todo.save()
            return redirect("todo")
    else:
        form = TodoForm() 

    todos = Todo.objects.all()
    return render(request, "todo.html", {'form': form, 'todos': todos})

def update_todo_complete(request, pk):
    if request.method == "POST":
        try:
            todo = Todo.objects.get(pk=pk)
            todo.status = True
            todo.save()
            return redirect("todo")
        except Todo.DoesNotExist:
            return redirect("todo")

    todos = Todo.objects.all()
    return render(request, "todo.html", {'todos': todos})

def Delete_item(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect("todo")
    return redirect("todo")