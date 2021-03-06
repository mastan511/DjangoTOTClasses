from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Student

# Create your views here.
def addStudent(request):
	if request.method == "POST":
		roll = request.POST.get('rollno')
		nm = request.POST.get('name')
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
		mb = request.POST.get('mobile')
		em = request.POST.get('email')
		add = request.POST.get('address')
		Student.objects.create(rollno = roll,name=nm,age=ag,gender=gen,branch=br,language=y,mobileno=mb,email=em,address=add)
		return redirect('read')
	return render(request,'db/addstudent.html')

def read(request):
	datas = Student.objects.all()
	context = {'data':datas}
	return render(request,'db/read.html',context)

def update(request,id):
	info = Student.objects.get(id = id)
	if request.method == 'POST':
		info.rollno =request.POST.get('rollno')
		info.name = request.POST.get('name')
		info.age = request.POST.get('age')
		info.gender = request.POST.get('gender')
		info.branch = request.POST.get('branch')
		info.language = request.POST.get('language')
		info.mobileno = request.POST.get('mobile')
		info.email = request.POST.get('email')
		info.address = request.POST.get('address')
		info.save()
		return redirect('read')
	return render(request,'db/update.html',{'info':info})

def delete(request,id):
	k = Student.objects.get(id=id)
	if request.method == 'POST':
		k.delete()
		return redirect('read')
	return render(request,'db/delete.html',{'k':k})
