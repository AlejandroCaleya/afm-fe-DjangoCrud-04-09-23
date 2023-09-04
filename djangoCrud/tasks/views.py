from django.shortcuts import render

# Create your views here.
def tasks(request):
    return render(request,'tasks.html')

def create(request):
    return render(request,'create.html')

def updatear(request):
    return render(request,'updatear.html')

def delete(request):
    return render(request,'delete.html')