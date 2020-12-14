from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
	return render(request,'bt/home.html')
def bttask(request):
	if request.method == 'POST':
		fname = request.POST['firstname']
		lname = request.POST['lastname']
		email = request.POST['email']
		mobile = request.POST['mobile']
		u = request.POST['username']
		p = request.POST['password']
		return render(request,'bt/details.html',{'fn':fname,'ln':lname,'mail':email,'phone':mobile,'us':u,'ps':p})
	return render(request,'bt/boottask.html')
def regtask(request):
	return render(request,'bt/regtask.html')
def regd(request):
	if request.method == 'POST':
		u = request.POST['usname']
		p = request.POST['pswd']
		if u=="Admin" and p == '1234':
			return render(request,'bt/details.html',{'us':u,'ps':p})
		else:
			return HttpResponse("Invalid Username or Password")
		# print(u,p)
		#return HttpResponse("Hi Username is: {}".format(u))
	
	return render(request,'bt/login.html')