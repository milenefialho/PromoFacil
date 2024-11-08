from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario
from django.shortcuts import redirect

def login(request):
	return HttpResponse('login')

def cadastro(request):
	return render(request, 'cadastro.html')

def valida_cadastro(request):
	nome = request.POST.get('nome')
	email = request.POST.get('email')
	senha = request.POST.get('senha')

	

	usuario = Usuario (nome= nome, senha = senha, email=email)
	usuario.save()

	return HttpResponse(f"{nome} {email} {senha}")
'''
	usuario = Usuario.objects.filter(email=email)
	if len(usuario) > 0:
		return redirect('/auth/login/')
	try:
		

		return redirect('auth/login/')

	except:
		retunr redirect('auth/cadastro/?status=1')
'''
	