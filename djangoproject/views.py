from django.shortcuts import HttpResponse,render,redirect
import random
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def register(request):
    error = None
    if request.method =="POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if User.objects.filter(username=username).exists():
            error = 'Username already exists'
        else:
            user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name)
            return redirect('/login')

    context = {
        'error':error
    }
    return render(request,'register.html',context)


def login_page(request):
    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')

    return render(request,'login.html')


def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/login')
    else:
        return redirect('/login')


def index(request,username):
    value = random.randint(1,100)

    return HttpResponse(f"HELLO FROM DJANGO , {value} , user is {username}")

def home(request):
    return HttpResponse("<h1>Welcome to my home page</h1>")

# @login_required()
def index_page(request):
    # if not request.user.is_authenticated:
    #     return redirect('/login')

    context ={
        "name":"RAM SHARMA",
        "age":15,
        "city":"DELHI",
        "hobbies":["SINGING","DANCING","CIRCKET",]
    }
    return render(request,'index.html',context)

@login_required()
def contact_page(request):
    return render(request,'contact.html')

def about_page(request):
    
    return render(request,'about.html')

def person_list(request):
    # request.GET['username'])
    # request.GET['username'])
    # request.GET['username'])
    # request.GET['username'])

    username = request.GET.get('username')
    age = request.GET.get('age')
    gender = request.GET.get('gender')




    persons = [
    {
        "name": "RAM",
        "age": 28,
        "gender": "Male"
    },
    {
        "name": "SHYAM ",
        "age": 32,
        "gender": "Female"
    },
    {
        "name": "GITA",
        "age": 24,
        "gender": "Female"
    },
    {
        "name": "SITA",
        "age": 29,
        "gender": "Female"
    },
    {
        "name": "RABIN",
        "age": 35,
        "gender": "Male"
    }
] 

    if username is not None and age is not None and gender is not None:

        person_dict = {} # person dictionary
        person_dict['name'] = username
        person_dict['age'] = age
        person_dict['gender'] = gender
        persons.append(person_dict)
    context = {
        'person_list':persons
    }
    

    return render(request,'person_list.html',context)


def calculate(request):
    # result = None
    num1 = None
    if request.method == 'POST':
        number1 = request.POST.get('number1')
        number2 = request.POST.get('number2')
        operation = request.POST.get('operation')

        if number1 is not None and number2 is not None and operation is not None:
            if operation  == "add":

                result = int(number1) + int(number2)
            elif operation == "subtract":
                result = int(number1) - int(number2)
            elif operation == "divide":
                try:
                    result = int(number1)/int(number2)
                except ZeroDivisionError:
                    result = "Error: Division by zero is not allowed"
            elif operation == 'multiply':
                result = int(number1) * int(number2)
            context  =  {'result':result}   
            return render(request,'result.html',context)

    elif request.method == "GET":
        # IF GET METHOD
        num1 = request.GET.get('num1') 
        result = "Please Calculate"
    # else:
    #     result = None
    context = {
        'num1':request.GET.get('num1'),
        'result':result

    }
    return render(request,'calculator.html',context)

