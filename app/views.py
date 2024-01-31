from django.shortcuts import render

# Create your views here.
from app.models import *

def equijoin(request):
    EO=Emp.objects.select_related('deptno').all()
    EO=Emp.objects.select_related('deptno').filter(empno__gt=7900)
    EO=Emp.objects.select_related('deptno').filter(sal__gt=3000)[:1:]
    EO=Emp.objects.select_related('deptno').filter(job='Salesman')
    EO=Emp.objects.select_related('deptno').filter(deptno__dloc='Dallas')
    EO=Emp.objects.select_related('deptno').filter(ename__in=('Allen','Scott'))
    EO=Emp.objects.select_related('deptno').filter(job__in=('Salesman','Manager'))



    d={'EO':EO}
    return render(request,'equijoin.html',d)