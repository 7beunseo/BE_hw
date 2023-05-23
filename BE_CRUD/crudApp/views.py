from django.shortcuts import render, redirect,get_object_or_404
from .models import *



def index(request):
    todo=Index.objects.all().order_by('-id')  #반대순서로 가져움 
    return render(request, "index.html",{"todo":todo})  #get요청시 


def create(request):
    if request.method=="POST":
        index=Index()
        index.title=request.POST.get("title")
        index.content=request.POST.get("content")
        index.save()
        return redirect("index")
    return render(request,"create.html")

def detail(request,id):
    todo=get_object_or_404(Index, pk=id)  #대문자로 써야함 !
    return render(request, "detail.html", {"todo":todo})

def update(request, id):
    update_todo=get_object_or_404(Index, pk=id) 
    if request.method=="POST":
        update_todo.title=request.POST.get("title")
        update_todo.content=request.POST.get("content")
        update_todo.date=request.POST.get('date')
        update_todo.save()
        return redirect("detail",update_todo.pk)
    return render(request, "update.html", {"update_todo":update_todo})

def delete(request, id):
    delete_todo=get_object_or_404(Index, pk=id)
    delete_todo.delete()
    return redirect("index")