from django.shortcuts import render
from app.models import Member
# Create your views here.

def index(request):
    members=Member.objects.all()
    context={'members':members}
    return render(request,'app/index.html',context)
