from django.http.response import HttpResponse
from django.shortcuts import render
from app.models import Member
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



