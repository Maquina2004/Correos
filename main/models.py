from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser

class UserManager(BaseUserManager):
    def create_user(self, correo,sexo=None, password=None,fecha_nacimiento=None,fecha_ingreso=None,nombre=None,apellido=None,rut=None,direccion=None,telefono=None,area_desempeno=None,cargo=None,carga_familiar=None, jefRRHH=False,trabRRHH=False, trabajador=True):
        if not correo:
            raise ValueError('deben tener correos')
        if not nombre:
            raise ValueError('Deben tener nombre')
        user = self.model(
            correo=self.normalize_email(correo), 
            nombre=nombre,
            apellido=apellido,
            sexo=sexo,
            rut=rut,
            fecha_nacimiento=fecha_nacimiento,
            fecha_ingreso=fecha_ingreso,
            direccion=direccion,
            telefono=telefono,
            area_desempeno=area_desempeno,
            cargo=cargo,
            carga_familiar=carga_familiar,

        )
        user.set_password(password)
        user.jefRRHH = jefRRHH
        user.trabRRHH = trabRRHH
        user.trabajador = trabajador
        user.save()
        return user

    def create_superuser(self, correo,nombre):
        user = self.create_user(correo,nombre)
        user.jefRRHH = False
        user.save()
        return user
class Usuario(AbstractBaseUser):
    SEXO_CHOICES=[('HOMBRE','Hombre'),('MUJER','Mujer'),('NO-ESPECIFICADO','No-especificado')]
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    sexo=models.CharField(max_length=20,choices=SEXO_CHOICES,default='NO-ESPECIFICADO')
    rut = models.CharField(max_length=12,unique=True)
    correo = models.EmailField(max_length=70,unique=True)
    fecha_nacimiento = models.DateField( max_length=50,unique=False,null=True)
    fecha_ingreso=models.DateTimeField(unique=True,auto_now_add=True)
    #Desde aqui se ve los privilegios de usuario
    jefRRHH = models.BooleanField(default=True) #Si quieres que el usuario a registrar sea jefe, dejalo en true
    trabRRHH = models.BooleanField(default=False)#Si quieres que sea trbajador de RRHH dejalo en true
    trabajador = models.BooleanField(default=False)#Si quieres que sea trabajador dejalo en true.
    #Hasta aqui se modifican los usuarios, que conste, que no puedes dejar todos en true, o si no te va a lanzar error SOLO UNO DEBE QUEDAR EN TRUE!!!!!!!!!!!!
    direccion=models.CharField(max_length=40)
    telefono=models.CharField(max_length=10)
    area_desempeno=models.CharField(max_length=15)
    cargo= models.CharField(max_length=15)
    cargaFamiliar=models.ForeignKey('cargaFamiliar',on_delete=models.CASCADE,null=True,blank=True)
    

    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = ['rut']

    objects= UserManager()


    def get_full_name(self):
        return self.correo

    def get_short_name(self):
        return self.correo

    def has_perm(self, perm, obj=None):
        "El usuario tiene un permiso especifico?"
        return True

    def has_module_perms(self, app_label):
        "El usuario tiene permisos para ver la aplicacion 'app_label'?"
        return True

    @property
    def is_staff(self):
        "El usuario es miembro del staff?"
        return self.staff

    @property
    def is_admin(self):
        "El usuario es un administrador?"
        return self.admin
    objects = UserManager()
    def __str__(self):
        return self.nombre

class cargaFamiliar(models.Model):
    PARENTEZCO_CHOICES=[('PADRE/MADRE','Padre o madre'),('HIJO/HIJA','Hijo o hija'),('CONYUGE','Pareja'),('NO-APLICA','No aplica')]
    rut= models.CharField(max_length=12,unique=True)
    nombre=models.CharField(max_length=10)
    apellido= models.CharField(max_length=20)
    parentezco=models.CharField(max_length=20,choices=PARENTEZCO_CHOICES,default='NO-APLICA')
    direccion= models.CharField(max_length=25)
    telefono=models.CharField(max_length=10)