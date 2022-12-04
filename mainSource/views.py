from threading import local
from django.shortcuts import redirect, render
from mainSource import DB
import random

localDB = DB.posecessorDBs()

def index(request):
    return render(request, 'index.html')
def login(request):
    return render(request, 'login.html')
def signup(request):
    return render(request, 'signup.html')
def landingPage(request):
    return render(request, 'landingPage.html')
def config(request):
    return render(request, 'config.html')
def result(request):
    return render(request, 'result.html')
def admin(request):
    return render(request, 'admin.html',{'content':localDB.show()})

def getInfoSignup(request):
    getName = request.GET['name']
    getPass = request.GET['password']
    localDB.add_user(getName, getPass)
    return redirect('login')

def checklogin(request):
    getName = request.GET['name']
    getPass = request.GET['password']
    condi = localDB.loginFunc(getName, getPass)
    if(condi == "admin"):
        return redirect('admin')
    if condi == "Login failed":
        return redirect('login')
    else:
        return redirect('index')
    
def showImage(request):
    image = localDB.pullImage()
    return render(request, 'result.html',{'image':image})

def getform(request):
    getName = request.GET['name']
    getPass = request.GET['password']
    localDB.add_user(getName, getPass)
    localDB.commiting()
    return redirect('admin')

def update(request):
    getUPName = request.GET['UPname']
    getid = request.GET['id']
    print(getid)
    localDB.updating(getUPName,getid)
    return redirect('admin')

def delete(request):
    getid = request.GET['ids']
    localDB.deleting(getid)
    return redirect('admin')