from django.shortcuts import HttpResponse,render
import random

def index(request,username):
    value = random.randint(1,100)

    return HttpResponse(f"HELLO FROM DJANGO , {value} , user is {username}")

def home(request):
    return HttpResponse("<h1>Welcome to my home page</h1>")


def index_page(request):

    context ={
        "name":"RAM SHARMA",
        "age":15,
        "city":"DELHI",
        "hobbies":["SINGING","DANCING","CIRCKET",]
    }
    return render(request,'index.html',context)

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

    number1 = request.GET.get('number1')
    number2 = request.GET.get('number2')
    operation = request.GET.get('operation')
    result = None
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

        
    # else:
    #     result = None
    context = {
        'result':result

    }
    return render(request,'calculator.html',context)

