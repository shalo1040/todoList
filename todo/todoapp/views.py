from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.htm')

def todo(request):
    return render(request, 'todo.htm')