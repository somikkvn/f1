from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .models import Service


def home(request):
	return render(request, 'ui/index.html', {})

def about(request):
	return render(request, 'ui/about.html', {})

def service(request):
	return render(request, 'ui/service.html', {})

def thanks(request):
	name = request.POST['name']
	email = request.POST['email']
	phone = request.POST['phone']
	selected = request.POST['selected']
	info = request.POST['info']
	element = Service(name = name, email = email, phone = phone, selected = selected, info = info)
	element.save()
	return render(request, 'ui/thanks.html', {'name': name,
											  'email': email,
											  'phone': phone,
											  'selected': selected,
											  'info': info})

def client_service(request):
	user = request.user
	user_service = Service.objects.filter(email=user.email).all()

	return render(request, 'ui/client_service.html', {'user_service':user_service})