from django.shortcuts import render
from correo.views import sendMail
from referido.models import PosibleReferido
# Create your views here.

def referirForm(request):
	return render(request, 'referido/referirForm.html')

def enviarInvitacion(request):

	mail = request.POST.get('mail', 0)
	nombre = request.POST.get('nombre', 0)
	if mail and nombre:
		p = PosibleReferido.objects.filter(correo = mail)
		if(len(p)):
			return render (request, 'main/principalview.html', { 'mensaje': 'Esta persona ya ha sido invitada' })
		p = PosibleReferido()
		

		try:
			p.auspiciador = request.user.username
			p.nombre = nombre
			p.correo = mail
			p.save()
		except:			
			return render (request, 'main/principalview.html', { 'mensaje': 'Este correo ya ha sido registrado' })			

		try:
			sendMail(mail, 'Invitacion mou.com.co', 'El usuario ' + request.user.username+ ' te ha enviado una invitacion')
		except:
			return render (request, 'main/principalview.html', { 'mensaje': 'No se pudo enviar el correo' })			
		
		
		referidos = PosibleReferido.objects.filter( auspiciador = request.user.username)
		
		if(len(referidos)):
			return render (request, 'referido/referidoview.html', { 'mensaje': 'Correo Enviado con exito', 'referidos' : referidos})
		
		return render (request, 'main/principalview.html', { 'mensaje': 'Correo Enviado con exito'})
		
	else:
		return render (request, 'main/principalview.html', { 'mensaje': 'Correo invalido'})