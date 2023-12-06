from django.shortcuts import render
from .models import *

# Create your views here.

def homepage(request):
    return render(request,'app/home.html')

def about(request):
    return render(request,'app/about.html')

def register(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        repassword = request.POST.get('password2')

        if password==repassword:
            reg=Register(name=name,email=email,password=password,repassword=repassword)
            print(reg)
            reg.save()
            return render(request,'app/login.html')
        else:
            data='Password and confirm password has not match'
            return render(request,'app/register.html',context=data)
    return render(request,'app/register.html')

def login(request):
        if request.method == 'POST':
            user = request.POST.get('username')
            pwrd = request.POST.get('password')
            User = Register.objects.get(name=user)
            
            if User.password == pwrd:
                request.session['username']=user
                data={'session':user}
                return render(request,'app/logout.html', context=data)
            else:
                data = {'status':"Incorrect Password!!!"}
                return render(request,'app/login.html',context=data)
        return render(request,'app/login.html')

def logout(request):
    if 'username' in request.session:
        del request.session['username']

    return render(request,'app/home.html')

def booking(request):
    if request.method == 'POST':
        department = request.POST.get('department')
        event = request.POST.get('event')
        date = request.POST.get('date')
        starttime = request.POST.get('starttime')
        endtime = request.POST.get('endtime')
        oname=request.session['username']

        obj=Books.objects.create(oname=oname,department=department,event=event,date=date,starttime=starttime,endtime=endtime)
        obj.save()
        user=request.session['username']
        if 'username' in request.session:
          user = request.session['username']
          data = {'session':user}
          return render(request,'app/logout.html',context=data)

    return render(request,'app/booking.html')

def history(request):
        if 'username' in request.session:
            event = Books.objects.all()
            data = {'event':event}
            return render(request,'app/history.html',context=data)
        else:
            data = {'status':'You need to login first'}
            return render(request,'login.html',context=data)