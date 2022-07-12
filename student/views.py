from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from student.models import Student
from .models import Mark
from .forms import MarksModelForm
# Create your views here.

def register_view(request):

        if request.method == 'POST':
            username = request.POST.get('username')
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            email = request.POST.get('email')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            print(username,fname,lname,email,password1,password2,"<---------")
            myuser = User.objects.create(username=username,password = password1)
            myuser.email = email
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.password=make_password(password2)
            myuser.save()        
        return render(request,'register.html')
    
        


def login_view(request):

        if request.method=="POST":
            username = request.POST['username']
            password = request.POST['password']
            print(username,password,"<---------")
            user = authenticate(username=username,password=password)
            print(user,"<----------")
            if user is not None:
                login(request,user)
                return redirect('/show')
            else:
                return HttpResponse("Invalid Credential..")
        return render(request,'login.html')
  
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/')
    return redirect('/show')

def show_student(request):
    if request.user.is_authenticated:
        data = Student.objects.all()
        d ={'data':data}
        return render(request,'show.html',context=d)
    else:
        return HttpResponse("<h2>Only Authenticated User Allowed..<h2><a href='/'>Back to Home</a>")

def add_student(request):
    if request.user.is_authenticated:
        Student.objects.bulk_create([
            Student(name='Vinay',email='vinaykushwaha588@gmail.com',mobile='9897675654',address='Satna MadhyaPradesh'),
            Student(name='Manoj Kumar',email='raj@gmail.com',mobile='9897675654',address='Sidhi MadhyaPradesh'),
            Student(name='Manoj Kushwaha',email='rkkushwaha2580@gmail.com',mobile='9897675654',address='Rewa MadhyaPradesh'),
            Student(name='Manoj Raj',email='vianojraj2580@gmail.com',mobile='9897675654',address='Shahdol MadhyaPradesh')
        ])
        return HttpResponse("<h2> Student Multiple Record Inserted<a href='/show'>Back To Home</a>")
    else:
        return HttpResponse("<h2>Only Authenticated User Allowed..<h2><a href='/'>Back to Home</a>")

def add_single(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            name = request.POST.get('name')
            mobile = request.POST.get('mobile')
            email = request.POST.get('email')
            address = request.POST.get('address')
            print(name,mobile,email,address,"<-------")
            Student.objects.create(name=name,mobile=mobile,email=email,address=address)
        return render(request,'addsingle.html')
    else:
        return HttpResponse("<h2>Only Authenticated User Allowed..<h2><a href='/'>Back to Home</a>")


def update_student(request,sid):
    if request.user.is_authenticated:
        stu = Student.objects.get(id=sid)
        if request.method=="POST":
            stu.name = request.POST.get('name')
            stu.mobile = request.POST.get('mobile')
            stu.email = request.POST.get('email')
            stu.address = request.POST.get('address')
            stu.save()
            return redirect('/show')
        d ={'stu':stu}    
        return render(request,'update.html',context=d)
    else:
        return HttpResponse("<h2>Only Authenticated User Allowed..<h2><a href='/'>Back to Home</a>")



def delete_view(request,sid):
    if request.user.is_authenticated:
        data = Student.objects.get(id=sid)
        data.delete()
        return redirect('/show')
    else:
        return HttpResponse("<h2>Only Authenticated User Allowed..<h2><a href='/'>Back to Home</a>")
    

def show_marks(request):
    if request.user.is_authenticated:
        mark = Mark.objects.all()
        d={'mark':mark}   
        return render(request,'showmarks.html',context=d)
    else:
        return HttpResponse("<h2>Only Authenticated User Allowed..<h2><a href='/'>Back to Home</a>")

def marks_student_delete(request,mid):
    if request.user.is_authenticated:
        mark = Mark.objects.get(id=mid)
        mark.delete()
        return redirect("/show")
    else:
        return HttpResponse("<h2>Only Authenticated User Allowed..<h2><a href='/'>Back to Home</a>")
def add_marks(request):
    if request.user.is_authenticated:
        form = MarksModelForm(request.POST)
        if request.method=="POST":
            if form.is_valid():
                form.save()                    
            return render(request,'form.html',{'form':form})
        else:
            return render(request,'form.html',{'form':form})
    else:
        return HttpResponse("<h2>Only Authenticated User Allowed..<h2><a href='/'>Back to Home</a>")
    
def marks_update(request,mid):
    if request.user.is_authenticated:
        mark = Mark.objects.get(id=mid)
        form = MarksModelForm(request.POST or None , instance=mark)
        if request.method=="POST":
            if form.is_valid():
                form.save()
                return redirect('/showmark')
            return render(request,'updatemark.html',{'form':form})
        else:
            return render(request,'updatemark.html',{'form':form})
    else:
        return HttpResponse("<h2>Only Authenticated User Allowed..<h2><a href='/'>Back to Home</a>")
            

# def marks_student_update(request,mid):
#     if request.user.is_authenticated:
#         mark = Mark.objects.get(id=mid)
#         if request.method=="POST":
#             mark.physics=request.POST.get('physics')
#             che.physics=request.POST.get('physics')
#             mark.physics=request.POST.get('physics')
#         return redirect("/show")
#     else:
#         return HttpResponse("<h2>Only Authenticated User Allowed..<h2><a href='/'>Back to Home</a>")
    