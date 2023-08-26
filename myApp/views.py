from django.shortcuts import render,redirect
from .models import destination,comments
from .forms import ArticleForm,CommentsForm


def home(request):
    dests= destination.objects.all()

    return render(request,'home.html',{'desti':dests})

def details(request,id):

    dest_selected=destination.objects.get(id=id)
    
    form = CommentsForm(instance=dest_selected)
    if request.method == "POST":
        form=CommentsForm(files=request.FILES,data=request.POST,instance=dest_selected)
        
        if form.is_valid():
           
           form.save()
           obj=form.instance
           return redirect('/list')
    context={}
   # context['dests']=dest_selected
    context={'dests':dest_selected,'form':form}
    return render(request,'details.html',context)


def listAll(request):
    dests=destination.objects.all()
    return render(request,'list.html',{'dests':dests})



def create(request):
   
    form = ArticleForm()
    if request.method == "POST":
        form=ArticleForm(files=request.FILES,data=request.POST)
        
        if form.is_valid():
           
           form.save()
           obj=form.instance
           return render(request,"create.html",{"obj":obj})
    else:
        print(form.errors)
    
    context = {'form':form}

    return render(request,'create.html',context)


def update(request,id):
    
    dests= destination.objects.get(id=id)
    form=ArticleForm(instance=dests)
    context={'form':form}
    if request.method == "POST":
        form=ArticleForm(files=request.FILES,data=request.POST,instance=dests)
        
        if form.is_valid():
           
           form.save()
           obj=form.instance
           return redirect('/list')
    else:
        print(form.errors)
    
    context = {'form':form}


    
    return render(request,'create.html',context)



def delete(request,id):
    dests= destination.objects.get(id=id)
    if request.method =="POST":
        dests.delete()
        return redirect('/list')
    context ={'dests':dests}
    return render(request,"delete.html",context)

# Create your views he