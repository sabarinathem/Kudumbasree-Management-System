from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from app.models import Member, Savings
from app.form import SavingForm,MemberForm
# Create your views here.
import datetime
from app.month import months


def startpage(request):
    return render(request,'app/startpage.html')
def index(request):
   
    members=Member.objects.all()
    context={'members':members}
    return render(request,'app/index.html',context)
def add_member(request):
    if request.method=="POST":
        form=MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("success")
    form=MemberForm()
    context={'form':form}
    return render(request,'app/add_member.html',context)

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
                return redirect('app:successful')
    except:
        if request.method=="POST":
            month=request.POST["month"]
            year=request.POST["year"]
            
            #take previous month balance of member
            m=int(months(month))-1
            y=int(year)
            if m==0:
                m=12
                y=y-1
                
            
            d=datetime.datetime(y,m,12)
            prev_month=d.strftime("%B")
        
            form=SavingForm(request.POST)
            if form.is_valid():
                sav=form.save(commit=False)
                member=Member.objects.get(id=id)
                try:
                    
                    yea=str(y)
                    prev_year=yea
                    prev_saving=Savings.objects.get(member=member,month=prev_month,year=prev_year)
                    sav.previous_month_balance=prev_saving.total_savings
                    prev_mon=prev_saving.total_savings
                    print(prev_mon)
                    
                except:
                    sav.previous_month_balance=0
                    prev_mon=0
                
                sav.member=member
                sav.month=month
                sav.year=year
                
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

                sav.savings_of_this_month=total_savings_this_month
                sav.total_savings=total_savings_this_month+prev_mon
                sav.save()


                return redirect('app:successful')

def show(request):
    savings=Savings.objects.all()
    context={'savings':savings}
    return render(request,'app/show.html',context)

def savings_of_intended_month(request):
    if request.method=="POST":
        mon=request.POST["month"]
        yea=request.POST["year"]
        monthsavings=Savings.objects.filter(month=mon,year=yea)
        monthsum=0
        for i in monthsavings:
            monthsum=monthsum+i.savings_of_this_month
        totalsum=0
        for j in monthsavings:
            totalsum=totalsum+j.total_savings
        # totalsavings=Savings.objects.all()
        # totalsum=0
        # for j in totalsavings:
        #     totalsum=totalsum+j.total_savings
        context={'savings':monthsavings,'month':mon,'year':yea,'total_savings_of_this_month':monthsum,'totalsavings':totalsum}
        return render(request,'app/show_savings_of_intended_month.html',context)
    date=datetime.datetime.now()
    y=int(date.strftime("%Y"))
    context={'range':range(y-10,y+10)}
    return render(request,'app/savings_of_intended_month.html',context)


