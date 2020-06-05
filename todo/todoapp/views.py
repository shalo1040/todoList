from django.shortcuts import render, get_object_or_404, redirect
from .models import Todo

# Create your views here.
def home(request):
    return render(request, 'home.htm')

def todo(request):
    todos = Todo.objects
    return render(request, 'todo.htm', {'todos':todos})

def detail(request, todo_id):
    todo_detail = get_object_or_404(Todo, pk=todo_id)
    return render(request, 'detail.htm', {'todo':todo_detail})

def new(request):
    return render(request, 'new.htm')

def create(request):
    todo = Todo()
    todo.title = request.GET['title']
    todo.time = request.GET['date']
    todo.time += " " + request.GET['time']
    todo.body = request.GET['body']
    todo.save()
    return redirect('/detail/'+str(todo.id))

def delete(request, todo_id):
    todo_detail = get_object_or_404(Todo, pk=todo_id)
    todo_detail.delete()
    return redirect('todo')

def edit(request, todo_id):
    if(request.method == 'POST'):
        todo_detail = get_object_or_404(Todo, pk=todo_id)
        date = "2020-06-" + str(todo_detail.time)[8:10]
        time = str(todo_detail.time)[11:13] + ":" + str(todo_detail.time)[14:16]
        return render(request, 'edit.htm', {'todo':todo_detail, 'date':date, 'time':time})

def update(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    if(request.method == 'POST'):
        todo.title = request.POST['title']
        todo.time = request.POST['date']
        todo.time += " " + request.POST['time']
        todo.body = request.POST['body']
        todo.save()
        return redirect('/detail/' + str(todo.id))