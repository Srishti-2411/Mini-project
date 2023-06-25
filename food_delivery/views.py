from django.shortcuts import render
from django.http import HttpResponse
import sqlite3
# Create your views here.
def Index(request):
    return render(request, 'index.html')

def About(request):
    return render(request, 'about.html')     

def Contact(request):
    return render(request, 'Contact.html')

def Shop(request):
    return render(request, 'Shop.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    
    return render(request, 'register.html')

def reg_done(request):
    db = sqlite3.connect('Registration')
    rs = db.cursor()

    rs.execute('''insert into register values('logan', '@gmail.com','2537849026', 'logan1234#' )''')
    db.commit()

    #rs.execute('''create table Register(name varchar(50), email varchar(100), phone varchar(10), passwd varchar(10))''')
    #db.commit()

    data = []
    rs.execute('select * from register')
    for i in rs:
        data.append(i)
        print(i)
    return render(request, 'reg_done.html', {'data': data})




