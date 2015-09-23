from django.shortcuts import render
from django.contrib.auth import authenticate, login
from autenticacion.forms import userLoginForm
from django.shortcuts import redirect
from django.contrib.auth.models import User
from usuario.models import Perfil
from correo.views import sendMail
from django.http import HttpResponse
from referido.models import PosibleReferido
# Create your views here.

def createUser(request):
	usuario = request.POST.get('user', 0)
	password = request.POST.get('password', 0)
	mail = request.POST.get('mail', 0)
	if usuario and password and mail:	

		if User.objects.filter(email = mail):
			return render(request, 'autenticacion/errorview.html', { 'mensaje': 'Este usuario ya existe'})

		try:
			user = User.objects.create_user(usuario, mail, password)
			user.save()				

		except :
			return render(request, 'autenticacion/errorview.html', { 'mensaje': 'Este usuario ya existe'})

		try:
			sendMail(mail, 'Usuario Registrado', 'Su usuario ' + usuario+ 'ha sido creado con exito.')
		except:
			return render(request, 'autenticacion/errorview.html', { 'mensaje': 'Problema al enviar correo'})

		try:
			u = User.objects.filter(username = usuario)
			#return HttpResponse(u[0].email)
			p = Perfil()
			p.user = user
			p.save()

		except:
			return render(request, 'autenticacion/errorview.html', { 'mensaje': 'Problema al crear perfil'})

		request.session['autenticado'] = 1
		user = authenticate(username=usuario, password=password)
		login(request, user)

		posibleReferido = PosibleReferido.objects.filter(correo = request.user.email )
		
		if (len(posibleReferido)):
			p_auspiciador = posibleReferido[0].auspiciador
			posibleReferido[0].estado = True
			posibleReferido[0].save()
			
			
			
			return render (request, 'main/principalview.html', { 'p_auspiciador': p_auspiciador  })
		return render (request, 'main/principalview.html')
		
	else:
		request.session['error'] = 'Formulario Invalido'
		return redirect('/login/error/')
