from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import Movie
from .forms import MovieForm


# Create your views here.
def movies(request):
    if request.method == 'GET':
        return render(request,'movie.html')
    else:
        name = request.POST['name']
        actor = request.POST['actor']
        story = request.POST['story']
        redate = request.POST['redate']
        Movie.objects.create(name=name,actor=actor,story=story,redate=redate)
        return HttpResponse('values inserted') 
    
def read_element(request):
    objs = Movie.objects.all()
    return render(request,'read.html',{'objs':objs})
def deletes(request,id):
    Movie.objects.get(id=id).delete()
    return redirect('read')
def up(request,id):
    if request.method == 'GET':
        ob = Movie.objects.get(id=id)
        return render(request,'update.html',{'ob':ob})
    else:
        name = request.POST['name']
        actor = request.POST['actor']
        story = request.POST['story']
        redate = request.POST['redate']
        Movie.objects.filter(id=id).update(name=name,actor=actor,story=story,redate=redate)
        return redirect('read')
def forms_insert(request):
    if request.method == 'GET':
        objs = MovieForm()
        return render(request,'forms.html',{'objs':objs}) 
    else:
        ch = MovieForm(request.POST)
        if ch.is_valid():
            ch.save()
            return redirect('read')
        else:
            return redirect('form')





    
