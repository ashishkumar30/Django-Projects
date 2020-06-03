from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .models import Members 

def home(request):
    return render (request, 'index.html')

def createresume(request):
    return render(request, 'index4x.html')


def uploadresume(request):
    return render(request, 'form2.html')

def templateresumeopen(request):
    return render(request, 'new 1.html')
def tohome(request):
    return render(request, 'index.html')

# def create(request):
#     #return render(request, 'index.html')
#     #print("hye")
#     return HttpResponse('<h1>Page was found</h1>')

def create(request):
    # Member = Members(

    #     i_name=request.POST['name'],
    #     i_email=request.POST['email'],
    #     i_subject=request.POST['subject'],
    #     i_message=request.POST['message'],
    #           )
    # Member.save()
    
    return HttpResponse('<h3> Message Send ! Please go back </h3>')
    #return redirect('/home/')
    #return render ( request,'/' )
