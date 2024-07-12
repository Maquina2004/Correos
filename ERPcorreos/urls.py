"""
URL configuration for ERPcorreos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main.views import RegisterView,Inicio,Lista,LoginView,Menu,verPerfil,modificarUsuario,registrarCarga
from administracion.views import indexAdmin,gestionTrabajadores,eliminarTrabajador,buscarTrabajador
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Inicio, name='Inicio'),
    path('lista/',Lista),
    path('Login/',LoginView.as_view(),name='Login'),
    path('Register/',RegisterView.as_view(),name='Register'),
    path('Menu/<int:id>', Menu),
    path('Administracion/',indexAdmin),
    path("Gestion/",gestionTrabajadores),
    path("Logout/",LogoutView.as_view(template_name='inicio.html'), name='Logout'),
    path("Perfil/<int:id>",verPerfil),
    path("ModificarDatos/<int:id>",modificarUsuario),
    path("EliminarTrabajador/<int:id>",eliminarTrabajador),
    path("Cargas/<int:id>",registrarCarga),
    path("buscarEmpleado/",buscarTrabajador, name="buscarEmpleado")
]
