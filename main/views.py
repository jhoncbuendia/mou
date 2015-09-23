from django.shortcuts import render
from referido.models import PosibleReferido
from usuario.models import Perfil
from django.http import HttpResponse	
# Create your views here.

def indexView(request):
	if request.session.get('autenticado', 0) == 0:
		return render (request, 'main/index.html')

	if request.session.get('autenticado', 0) == 1:
		p_referidos = PosibleReferido.objects.filter ( auspiciador =  request.user.username )
		#perfil = Perfil.objects.filter( user = request.user)[0]
		posibleReferido = PosibleReferido.objects.filter(correo = request.user.email )
		#return HttpResponse(posibleReferido[0].auspiciador)

		#if perfil.auspiciador == '':
			#return HttpResponse('vacio')
		if (len(posibleReferido)):
			p_auspiciador = posibleReferido[0].auspiciador
			return render (request, 'main/principalview.html', { 'p_referidos' : p_referidos, 'p_auspiciador': p_auspiciador  })
		else:
			return render (request, 'main/principalview.html', { 'p_referidos' : p_referidos })
