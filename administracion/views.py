from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from main.models import *
from administracion.forms import *
from django.views.generic import CreateView 

def Inicio (request):
 return  render(request, "inicio.html") #TUVE QUE COLOCAR ESTA VISTAS PORQUE OSINO ME DABA ERROR


def Lista (request):
 lista=Usuario.objects.all()
 data={
  'trabajadores':lista
 }
 
 return  render(request, "listempl.html",data)


@login_required
def indexAdmin(request):
    return render (request,'indexAdmin.html')

@login_required
def gestionTrabajadores(request):
    trabajadores= Usuario.objects.all()
    if request.method=='POST':
        user= request.POST.get('Userid',False)
        jefRRHH=request.POST.get('jefRRHH',False)
        trabRRHH=request.POST.get('trabRRHH',False)
        trabajador=request.POST.get('trabajador',False)
        if jefRRHH:
            jefRRHH=True
        if trabRRHH:
            trabRRHH=True
        if trabajador:
            trabajador=True   
        userchange= Usuario.objects.get(id=user)
        userchange.jefRRHH=jefRRHH
        userchange.trabjRRHH=trabRRHH
        userchange.trabajador=trabajador
        userchange.save()    
        return redirect('/GestionTrabajadores/')
    return render (request,'gestionTrabajadores.html',{'trabajadores':trabajadores})

@login_required
def eliminarTrabajador(request,id):
    if request.user.jefRRHH:
        trabajador= Usuario.objects.get(id=id)
        trabajador.delete()
    return redirect('/Gestion/')

@login_required
def buscarTrabajador (request):
    resultado = None

    if request.method == 'POST':
        form = BusquedaTrabajadorForm(request.POST)

        if form.is_valid():
            rut = form.cleaned_data['rut']
            try:
                resultado = Usuario.objects.get(rut=rut)
            except Usuario.DoesNotExist:
                resultado = None
    else:
        form = BusquedaTrabajadorForm()

    return render(request, 'buscarEmpleado.html', {'form': form, 'trabajador': resultado})
