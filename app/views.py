from django.http.response import HttpResponse
from django.shortcuts import render
from app.models import Member, Savings
from app.form import SavingForm
# Create your views here.
import datetime

def index(request):
    members=Member.objects.all()
    context={'members':members}
    return render(request,'app/index.html',context)

def select_month_and_year(request,id):
    member=Member.objects.get(id=id)
    date=datetime.datetime.now()
    y=int(date.strftime("%Y"))
    context={'member':member,'range':range(y-10,y+10)}
    return render(request,'app/select_month_and_year.html',context)

def add_or_update_savings(request,id):
    try:
        if request.method=="POST":
            month=request.POST["month"]
            year=request.POST["year"]
            print(type(month),type(year))
            
        member=Member.objects.get(id=id)
        saving=Savings.objects.get(member=member,month=month,year=year)
        form=SavingForm(instance=saving)
        context={'form':form,'member':member}
    except:
        if request.method=="POST":
            month=request.POST["month"]
            year=request.POST["year"]
            print(type(month),type(year))
            
        member=Member.objects.get(id=id)
      
        form=SavingForm()
        context={'form':form,'member':member}

    return render(request,'app/add_or_update_savings.html',context)

