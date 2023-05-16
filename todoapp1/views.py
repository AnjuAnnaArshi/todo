from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import task
from .forms import todoform
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView


class tasklist(ListView):
    model = task
    template_name = 'home.html'
    context_object_name = 't'

class taskdetails(DetailView):
    model = task
    template_name = 'details.html'
    context_object_name = 'task'

class taskupdate(UpdateView):
    model = task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('detailview',kwargs={'pk':self.object.id})

class deleteview(DeleteView):
    model = task
    template_name = 'delete.html'
    success_url = reverse_lazy('classhome')

# Create your views here.
def home(request):
    tasks = task.objects.all()
    if request.method=='POST':
        ta=request.POST.get('task','')
        p=request.POST.get('priority','')
        d=request.POST.get('date','')
        t=task(name=ta,priority=p,date=d)
        t.save()
        # return redirect('/')
    return render(request,'home.html',{'t':tasks})

# def details(request):
#     tasks=task.objects.all()
#     return render(request,'details.html',{'t':tasks})

def delete(request,taskid):
    if request.method=='POST':
        t=task.objects.get(id=taskid)
        t.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,taskid):
    t=task.objects.get(id=taskid)
    f=todoform(request.POST or None,instance=t)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'f':f,'t':t})

