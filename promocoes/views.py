from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

# Create your views here.

def home(request):
	if request.session.get('usuario'):
		return HttpResponse('Olá')
	else:
		return redirect('/auth/login/?status=2')
