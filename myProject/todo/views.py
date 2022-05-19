from cgitb import text
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST
from .models import Todo
from .forms import TodoForm

def index(request):
    todo_list = Todo.objects.order_by('id')
    
    form = TodoForm()
    
    context = {'todo_list': todo_list, 'form': form}
    return render(request, 'todo/index.html', context)

@require_POST
def addTodo(request):
    form = TodoForm(request.POST)
    print(request.POST['text'])
    
    if form.is_valid:
        todo_new = Todo(text = form.cleaned_data['text'])
        todo_new.save()
        
    return redirect('index')

def complete(request, todo_id):
    
    comp = Todo.objects.get(pk=todo_id)
    comp.completed = True
    comp.save()
    
    return redirect('index')

def deleteCompleted(request):
    
    var = Todo.objects.filter(completed__exact = True)
    var.delete()
    
    return redirect('index')

def deleteAll(request):
    
    Todo.objects.all().delete()
    
    return redirect('index')