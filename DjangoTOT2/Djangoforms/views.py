from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee

# Create your views here.
from Djangoforms.forms import DynamicHtmlFormGen

def dynamichtmlformgen(request):
	t = DynamicHtmlFormGen()
	return render(request,'DJF/dynamichtmlformgen.html',{'form':t})

def addEmployee(request):
	if request.method == "POST":
		fm = request.POST.get('firstname')
		lm = request.POST.get('lastname')
		ag = request.POST.get('age')
		gen = request.POST.get('gender')
		br = request.POST.get('branch')
		lang = request.POST.getlist('language')
		lan=""
		for i in lang:
			if lang.index(i)==0:
				lan+=i
			else:
				lan+=','+i
		y = lan
		em = request.POST.get('email')
		Employee.objects.create(firstname = fm,lastname=lm,age=ag,gender=gen,branch=br,language=y,email=em)
	return render(request,'db/dynamichtmlformgen.html')

# def read(request):
# 	datas = Student.objects.all()
# 	context = {'data':datas}
# 	return render(request,'db/read.html',context)
