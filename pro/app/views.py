from django.shortcuts import render,redirect, get_object_or_404
from .models import Cust,Task
# Create your views here.
def index(request):
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            cus= Cust.objects.filter(username=username, password=password).exists()
            if cus:
                return redirect('tasklist')
        return render(request,"index.html")
def tasklist(request):
     a=Task.objects.all()
     return render(request,"tasklist.html",{'a':a})
def update(request,id):
    if request.method == 'POST':
        title=request.POST.get('title')
        description=request.POST.get('description')
        duedate=request.POST.get('duedate')
        status=request.POST.get('status')
        edit=Task.objects.get(id=id)
        edit.title=title
        edit.description=description
        edit.duedate=duedate
        edit.status=status
        edit.save()
        return redirect('tasklist')
    return render(request,"update.html")
def taskcreation(request):
    if request.method == "POST":
        title=request.POST.get('title')
        description=request.POST.get('description')
        duedate=request.POST.get('duedate')
        status=request.POST.get('status')
        username=request.POST.get('username')
        fm=Task(username=username,title=title,description=description,duedate=duedate,status=status)
        fm.save()
        return redirect('tasklist')
    return render(request,"taskcreation.html")

def delete(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect('tasklist')