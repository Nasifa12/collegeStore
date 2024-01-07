from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth


# Create your views here.
def home(request):
    return render(request, "home.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already exist')
                return redirect('register')

            else:
                user = User.objects.create_user(username=username, password=password)
                user.set_password(password)
                user.save();

                return redirect('login')
        else:
            messages.info(request, 'Password not matching')
            return redirect('register')
    else:
        print("this is no post method")
    return render(request, "register.html")


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid Credentials")
            return redirect('login')
    return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect('/')


def detail(request):
    if request.method == 'POST':
        name = request.POST['Name']
        dob = request.POST['DOB']
        age = request.POST['Age']
        gender = request.POST['Gender']
        phone_number = request.POST['Phone_number']
        mail_id = request.POST['Mail_ID']
        address = request.POST['Address']
        department = request.POST['Department']
        courses = request.POST['Courses']
        purpose = request.POST['Purpose']
        materials = request.POST['Materials']

        user = User.objects.create_user(name=Name, dob=DOB, age=Age, gender=Gender, department=Department,
                                        phone_number=Phone_number, mail_id=Mail_ID, address=Address, courses=Courses,
                                        purpose=Purpose, materials=Materials)
        user.save();
        messages.info(request, 'Order Confirmed')
        return redirect('detail')
    return render(request, "detail.html")
