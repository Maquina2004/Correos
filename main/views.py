from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,FormView
from django.contrib.auth import authenticate, login
from main.forms import *
from main.models import *

def Inicio (request):
 
 return  render(request, "inicio.html")

def Lista (request):
 lista=Usuario.objects.all()
 data={
  'trabajadores':lista
 }
 
 return  render(request, "listempl.html",data)

class RegisterView (CreateView):
    form_class=formularioRegistro
    template_name='register.html'
    success_url='/Menu/'
    success_message="%(name)s Se ha creado exitosamente"
    def form_valid(self, form):
        print(len(self.request.POST['rut']))
        request=self.request
        print(len(self.request.POST['rut']))
        login(request,form.save())
        if request.user.jefRRHH:
            return redirect ('/Administracion/')
        return redirect('/Menu/'+str(request.user.id))

class LoginView(FormView):
  form_class= LoginForm
  template_name= 'login.html'
  success_url='/Menu/'
  def form_valid(self, form):
      request=self.request
      correo=form.cleaned_data.get("correo")
      password=form.cleaned_data.get("password")
      user=authenticate(request,username=correo,password=password)
      if user is not None:
        login(request,user)
        if user.jefRRHH or user.trabRRHH:
            return redirect ('/Administracion/')
        return redirect ('/Menu/'+str(user.id))
      return super(LoginView,self).form_invalid(form)
  

@login_required
def modificarUsuario(request,id):
    trabajador=Usuario.objects.get(id=id)
    form=modificarUserform(instance=trabajador)
    if request.method=='POST':
        form=modificarUserform(request.POST, instance=trabajador)
        if form.is_valid():
            form.save()
        return redirect('/Perfil/'+str(id))
    return render (request,'modificarUsuario.html',{'form':form})

@login_required
def Menu(request,id):
    trabajador=Usuario.objects.get(id=id)
    
    return render (request,'menu.html')

@login_required
def verPerfil(request,id):
    trabajador= Usuario.objects.get(id=id)
    carga=trabajador.cargaFamiliar
    modCarga=cargaFamiliarForm(request.POST or None,instance=carga)
    if request.method=='POST':
        modCarga=cargaFamiliarForm(request.POST or None,instance=carga)
        if modCarga.is_valid():
            modCarga.save()
        return redirect('/Perfil/'+str(id))
    return render(request,'verPerfil.html',{'trabajador':trabajador,'carga':carga,'form':modCarga})

@login_required
def registrarCarga(request,id):
    trabajador=Usuario.objects.get(id=id)
    formulario=cargaFamiliarForm()
    if request.method=='POST':
        formulario=cargaFamiliarForm(request.POST)
        if formulario.is_valid():
            carga_familiar=formulario.save(commit=False)
            carga_familiar.usuario=trabajador
            carga_familiar.save()
            trabajador.cargaFamiliar=carga_familiar
            trabajador.save()
            return redirect ('/Perfil/'+str(id))
    return render(request,'cargasRegister.html',{'form':formulario})