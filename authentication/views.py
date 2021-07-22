from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash, login, authenticate
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from paytm import Checksum
from django.contrib.auth.decorators import login_required

# Create your views here.
def userLogin(request):
	if request.method=='POST':
		return_url = request.POST.get('next')
		username = request.POST['email']
		password = request.POST['password']
		user = auth.authenticate(username=username, password=password)
		print(user)
		if user is not None:
			auth.login(request, user)
			if return_url:
				return redirect(return_url)
			else:
				return redirect('/')
		else:
			messages.info(request,'Invalid username or password')
			return render(request,'login.html')

	else:	
		if request.user.is_authenticated:
			return redirect('/')
		return render(request,'login.html')


def signUp(request):
	if request.method == 'POST':
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		email = request.POST['email']
		username = request.POST['email']
		password = request.POST['password']
		confirm_password = request.POST['confirm_password']
		if password == confirm_password and password != "":
			if User.objects.filter(username=username).exists():
				print("=================email address is already registered===========")
				messages.info(request,'This E-mail is already registered.')
				return redirect('authentication:sign_up')	
			else:
				try:
					user = User.objects.create_user(username = username, password=password, email=email, first_name=first_name, last_name=last_name)
					print("user------------- ",user)
					user.save()
				except:
					print("Exception")
				else:
					print("==============================User created=====================")
					new_user = authenticate(username=username, password=password)
					if new_user is not None:
						login(request, new_user)
					return redirect('/')
			
		else:
			print("==============================password is not matching=========")
			messages.info(request,'passwrods are not matching')
			return redirect('authentication:sign_up')
		return redirect('authentication:sign_up')
	else:
		if request.user.is_authenticated:
			return redirect('/')
		return render(request,'sign_up.html')
def logout(request):
	auth.logout(request)
	return redirect('/')



