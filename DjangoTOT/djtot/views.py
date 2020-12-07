from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
	return HttpResponse("Hi Welcome user")

def fun(r):
	return HttpResponse("<h2 style='background-color:green;'> Hello GoodAfternoon </h2>")


def rc(y,name):
	return HttpResponse("<h2>Hi welcome {}</h2>".format(name))

def mulTable(s,n):
	l = ""
	for i in range(1,11):
		v = n*i
		l+=str(n)+"*"+str(i)+"="+str(v)+"\n"
	return HttpResponse(l)
	
def myDetails(k,name,age):
	return render(k,'fy/home.html',{'n':name,'a':age})
def sample(request):
	return render(request,'fy/demo.html')
def myJs(request):
	return render(request,'fy/jsc.html')
def mylogin(request):
	return render(request,'fy/login.html')
def myreg(request):
	return render(request,'fy/reg.html')
def myarthematic(request):
	return render(request,'fy/arth.html')