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


def selfjoin(request):
    EMO=Emp.objects.select_related('mgr').all()
    EMO=Emp.objects.select_related('mgr').filter(mgr__ename='King')
    EMO=Emp.objects.select_related('mgr').filter(sal__gt=3000)
    EMO=Emp.objects.select_related('mgr').filter(mgr__sal__gt=3000)
    EMO=Emp.objects.select_related('mgr').filter(sal__lt=3000)
    EMO=Emp.objects.select_related('mgr').filter(mgr__sal__lt=3000)
    EMO=Emp.objects.select_related('mgr').filter(deptno=30)
    EMO=Emp.objects.select_related('mgr').filter(comm=None)
    EMO=Emp.objects.select_related('mgr').filter(hiredate__year=1980)
    EMO=Emp.objects.select_related('mgr').filter(mgr__hiredate__year=1981)
    EMO=Emp.objects.select_related('mgr').filter(ename__in=('Allen','Scott'))
    EMO=Emp.objects.select_related('mgr').filter(mgr__ename__in=('King','Scott'))
    EMO=Emp.objects.select_related('mgr').filter(job='Salesman')
    EMO=Emp.objects.select_related('mgr').filter(mgr__job='Manager')
    

    d={'EMO':EMO}
    return render(request,'selfjoin.html',d)