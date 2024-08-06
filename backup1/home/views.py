from django.shortcuts import render
from .models import Emp
def home(request):
    data=Emp.objects.all()
    return render(request,'index.html',{'data':data})