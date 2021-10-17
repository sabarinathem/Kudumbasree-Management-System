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
        context={'form':form,'member':member,'month':month,'year':year}
    except:
        if request.method=="POST":
            month=request.POST["month"]
            year=request.POST["year"]
            print(type(month),type(year))
            
        member=Member.objects.get(id=id)
      
        form=SavingForm()
        context={'form':form,'member':member,'month':month,'year':year}

    return render(request,'app/add_or_update_savings.html',context)
def save(request,id):
    try:
        if request.method=="POST":
            month=request.POST["month"]
            year=request.POST["year"]
            member=Member.objects.get(id=id)
            saving=Savings.objects.get(member=member,month=month,year=year)
            form=SavingForm(request.POST,instance=saving)
            if form.is_valid():
                sav=form.save(commit=False)
                previous_month_savings=saving.previous_month_balance
                if previous_month_savings==None:
                    previous_month_savings=0
                first_weak=saving.first_weak
                if first_weak==None:
                    first_weak=0
                second_weak=saving.second_weak
                if second_weak==None:
                    second_weak=0
                third_weak=saving.third_weak
                if third_weak==None:
                    third_weak=0
                fourth_weak=saving.fourth_weak
                if fourth_weak==None:
                    fourth_weak=0
                fifth_weak=saving.fifth_weak
                if fifth_weak==None:
                    fifth_weak=0
                total_savings_this_month=first_weak+second_weak+third_weak+fourth_weak+fifth_weak
                sav.savings_of_this_month=total_savings_this_month
                total_savings=previous_month_savings+total_savings_this_month
                sav.total_savings=total_savings
                sav.save()
                return HttpResponse(first_weak+second_weak+third_weak+fourth_weak+fifth_weak)
    except:
        if request.method=="POST":
            month=request.POST["month"]
            year=request.POST["year"]
            form=SavingForm(request.POST)
            if form.is_valid():
                sav=form.save(commit=False)
                member=Member.objects.get(id=id)
                sav.member=member
                sav.month=month
                sav.year=year
                sav.previous_month_balance=200
                first_weak=form.cleaned_data['first_weak']
                if first_weak==None:
                    first_weak=0
                second_weak=form.cleaned_data['second_weak']
                if second_weak==None:
                    second_weak=0
                third_weak=form.cleaned_data['third_weak']
                if third_weak==None:
                    third_weak=0
                fourth_weak=form.cleaned_data['fourth_weak']
                if fourth_weak==None:
                    fourth_weak=0
                fifth_weak=form.cleaned_data['fifth_weak']
                if fifth_weak==None:
                    fifth_weak=0
                total_savings_this_month=first_weak+second_weak+third_weak+fourth_weak+fifth_weak
                total_savings=total_savings_this_month
                sav.savings_of_this_month=total_savings_this_month
                sav.total_savings=total_savings
                sav.save()


                return HttpResponse(total_savings)


