from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache
from studentapp.models import City, Course, Student

# Create your views here.
# @login_required
# @never_cache
def forgetPassword(request):
    if request.method == 'POST':
        username = request.POST["tb_username"]
        email = request.POST["email"]
        if username == User.objects.filter(username=username) or email == User.objects.filter(email=email):
            data = {'username': username, "email": email }
        return redirect(request, 'forget.html', {'data': data})
    else:
        return render(request, 'forget.html')

def regdata(request):
    if request.method == 'POST':
        username = request.POST['tb-username']
        password = request.POST['tb-password']
        email = request.POST['tb-email']
        u2 = User.objects.filter(Q(username=username), Q(password=password), Q(email=email)).exists()
        if u2:
            return render(request, 'register.html', {'msg': 'User already Exist, Please Login!!!'})
        else:
            u1 = User.objects.create_superuser(username=username, password=password, email=email)
            u1.save()
            return redirect('log')
    else:
        return render(request, 'register.html', {'msg': ''})

def login_fun(request):
    if request.method == 'POST':
        u_name = request.POST['tb_username']
        password = request.POST['tb_password']
        user = authenticate(username=u_name, password=password)
        if user is not None:
            if user.is_superuser:
                login(request, user)
                request.session['Name'] = u_name
                return redirect('home')
        else:
            return render(request, 'login.html', {'msg': 'Enter correct Username and Password'})
    else:
        return render(request, 'login.html', {'msg': ''})

@login_required
@never_cache
def home_fun(request):
    return render(request, 'home.html', {'data': request.session['Name']})

@login_required
@never_cache
def insert(request):
    if request.method == 'POST':
        s1 = Student()
        s1.Student_name = request.POST['tb_name']
        s1.Student_phone = int(request.POST['tb_phone'])
        s1.Student_email = request.POST['tb_email']
        s1.Student_fees = int(request.POST['tb_fees'])
        s1.Student_course = Course.objects.get(course_name=request.POST['ddl_course'])
        s1.Student_city = City.objects.get(city_name=request.POST['ddl_city'])
        s1.save()
        return redirect('insert')
    else:
        city = City.objects.all()
        course = Course.objects.all()
        return render(request, 'insert.html', {'CityData': city, 'CourseData': course})

@login_required
@never_cache
def display(request):
    s1 = Student.objects.all()
    return render(request, 'display.html', {'data': s1})

@login_required
@never_cache
def update(request, id):
    s1 = Student.objects.get(id=id)
    city = City.objects.all()
    course = Course.objects.all()
    if request.method == 'POST':
        s1.Student_name = request.POST['tb-name']
        s1.Student_phone = int(request.POST['tb-phone'])
        s1.Student_email = request.POST['tb-email']
        s1.Student_fees = int(request.POST['tb-fees'])
        s1.Student_course = Course.objects.get(course_name=request.POST['ddl-course'])
        s1.Student_city = City.objects.get(city_name=request.POST['ddl-city'])
        s1.save()
        return redirect('display')
    else:
        return render(request, 'update.html', {'data': s1, 'CityData': city, 'CourseData': course})

@login_required
@never_cache
def delete_fun(request, id):
    s1 = Student.objects.get(id=id)
    s1.delete()
    return redirect('display')


def logout_fun(request):
    logout(request)
    return redirect('log')