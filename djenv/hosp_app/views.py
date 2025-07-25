from django.shortcuts import render,redirect
from .models import *


# Create your views here.
def index(request):
    return render(request,'index.html')

def viewDept(request):
    data = dept_tbl.objects.all()
    return render(request,"viewDept.html",{"data":data})

def viewDoc(request):
    data = doc_tbl.objects.all()
    return render(request,"viewDoc.html",{"data":data})

def addDept(request):
    msg = ""
    if request.method == "POST":
        name =request.POST.get("name")
        des =request.POST.get("des")
        obj=dept_tbl.objects.create(name=name,des=des)
        obj.save()
        if obj:
            msg = "added success"
            return render(request,"addDept.html",{'msg':msg})
        else:
            return render(request,"addDept.html",{'msg':msg})
    return render(request,'addDept.html',{'msg':msg})

def updateDept(request):
    dept_id = request.GET.get('cid')
    obj = dept_tbl.objects.get(pk=dept_id)
    
    if request.method == "POST":
        obj.name =request.POST.get("name")
        obj.des =request.POST.get("des")
        obj.save()
        return redirect("viewDept")
    return render(request,"updateDept.html",{'data':obj})

def delDept(request,id):
    obj = dept_tbl.objects.get(pk=id)
    obj.delete()
    return redirect("viewDept")

def registerUser(request):
    msg = ""
    if request.method == "POST":
        name =request.POST.get("name")
        mob =request.POST.get("mob")
        email =request.POST.get("email")
        password =request.POST.get("password")
        user_type =request.POST.get("user_type")
        obj=reg_tbl.objects.create(name=name,mob=mob,email=email,password=password,user_type=user_type)
        obj.save()
        if obj:
            msg = "added success"
            return render(request,"registerUser.html",{'msg':msg})
        else:
            return render(request,"registerUser.html",{'msg':msg})
    return render(request,"registerUser.html")

def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        obj = reg_tbl.objects.filter(email=email,password=password)
        if obj.exists():
            for i in obj : 
                request.session["id1"] = i.id
                request.session["name"] = i.name
                request.session["email"] = i.email
                request.session["mob"] = i.mob
                request.session["user_type"] = i.user_type
            obj = {"name": i.name}
            if i.user_type == "customer":
                return render(request,"customerHome.html",{"data":obj})
            elif i.user_type == "doctor":              
                return render(request,"docHome.html",{"data":obj})
            else :
                return render(request,"adminHome.html",{"data":obj})

    return render(request,"login.html")

def bookAppt(request):
    doct_obj = doc_tbl.objects.all()
    print(doct_obj)
    if 'id1' in request.session:
        user_id = request.session['id1']
    if 'name' in request.session:
        name = request.session['name']
    if 'email' in request.session:
        email = request.session['email']
    if 'mob' in request.session:
        mob = request.session['mob']
    my_dict = {"id":user_id,"name": name,"email" : email,"mob":mob,"doc":doct_obj,"msg":""}
    msg =""
    if request.method == "POST":
        user = reg_tbl.objects.get(id=user_id)

        name =request.POST.get("name")
        mob =request.POST.get("mob")
        email =request.POST.get("email")
        doc_name =request.POST.get("doc_name")
        test =request.POST.get("test")
        date=request.POST.get("date")
        gender=request.POST.get("gender")
        # format_string_1 ="%d-%m-%Y"
        # date = datetime.strptime(date_string, format_string_1).date()
        district =request.POST.get("district")
        obj=book_appt_tbl.objects.create(user=user,name=name,mob=mob,email=email,doc_name=doc_name,test=test,date=date,district=district,gender=gender)
        obj.save()
        if obj:
            msg = "added success"
            return render(request,"bookAppt.html",{'data' : my_dict})
        else:
            return render(request,"bookAppt.html",{'data' : my_dict})

    return render(request,"bookAppt.html",{'data' : my_dict})

def viewAppt(request):
    if 'id1' in request.session:
        user_id = request.session['id1']
    if 'user_type' in request.session:
        user_type = request.session["user_type"]
    if user_type == "admin":
        appt_obj = book_appt_tbl.objects.all()
    elif user_type == "customer":
        appt_obj = book_appt_tbl.objects.filter(user=user_id)
    else:
        appt_obj = book_appt_tbl.objects.all()
    
    return render(request,"viewAppt.html",{"data":appt_obj})