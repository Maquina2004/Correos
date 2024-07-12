from django import forms
from main.models import *
       

class formularioRegistro(forms.ModelForm):
    
    password= forms.CharField(label='Contraseña:' , widget=forms.PasswordInput(attrs={'placeholder':'Ingrese su contraseña','class':'form-control mt-2'}))
    password_2=forms.CharField(label='Repita la contraseña:', widget=forms.PasswordInput(attrs={'placeholder':'Re-ingrese su contraseña','class':'form-control mt-2'}))
    class Meta:
        model= Usuario
        fields=['correo','rut','nombre','apellido','direccion','telefono','area_desempeno','cargo','sexo']
        widgets={
            'rut':forms.TextInput(attrs={'placeholder':'Ingrese rut','label':'Cedula de identidad del trabajador','class':'form-control mt-2'}),
            'nombre':forms.TextInput(attrs={'placeholder':'Ingrese nombre','label':'Nombre del trabajador','class':'form-control mt-2'}),
            'correo':forms.TextInput(attrs={'placeholder':'Ingrese email ','label':'Email del trabajador','class':'form-control mt-2'}),
            'apellido':forms.TextInput(attrs={'placeholder':'Ingrese apellido','label':'Apellido paterno del trabajador','class':'form-control mt-2'}),
            'direccion':forms.TextInput(attrs={'placeholder':'Ingrese la direccion','label':'Direccion del trabajador.','class':'form-control mt-2'}),
            'telefono':forms.TextInput(attrs={'placeholder':'Ingrese telefono','label':'Cedula del trabajador','class':'form-control mt-2'}),
            'area_desempeno':forms.TextInput(attrs={'placeholder':'Ingrese lugar de trabajo','label':'Area de desmpeño del trabajador','class':'form-control mt-2'}),
            'cargo':forms.TextInput(attrs={'placeholder':'Escriba el cargo','label':'Cargo del trabajador','class':'form-control mt-2'}),

            
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields ['sexo'].widget.attrs.update({'class':'form-control mt-2'})
        
    def clean_email(self):
        email= self.cleaned_data.get('correo')
        qs=Usuario.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("El correo ya esta en uso")
        return email

    def clean(self):
        cleaned_data=super().clean()
        password= cleaned_data.get("password")
        password_2= cleaned_data.get("password_2")
        correo=cleaned_data.get("correo")
        rut = cleaned_data.get("rut")
        nombre=cleaned_data.get("nombre")
        apellido= cleaned_data.get("apellido")
        direccion= cleaned_data.get("direccion")
        telefono= cleaned_data.get("telefono")
        area_desempeno= cleaned_data.get("area_desempeno")
        cargo=cleaned_data.get("cargo")
        if correo is None:
            self.add_error('correo',"Debe proporcionar un correo")
        if len(password)< 8:
            self.add_error('password',"La contraseña debe ser mayor a 8 digitos")
        if password is not None and password != password_2:
            self.add_error('password_2',"Las contraseñas no coinciden")
        if nombre is None:
            self.add_error('nombre',"Debe rellenar este campo")
        if apellido is None:
            self.add_error('apellido',"Debe rellenar este campo")
        if direccion is None:
            self.add_error('direccion',"Debe rellenar este campo")
        if telefono is None:
            self.add_error('telefono',"Debe rellenar este campo")
        if area_desempeno is None:
            self.add_error('area_desempeno',"Debe rellenar este campo")
        if cargo is None:
            self.add_error('cargo',"Debe rellenar este campo")
        return cleaned_data
    def save(self,commit=True):
        correo=super().save(commit=False)
        correo.set_password(self.cleaned_data["password"])
        if commit:
            correo.save()
        return correo
       
class cargaFamiliarForm(forms.ModelForm):
    class Meta:
        model= cargaFamiliar
        fields=['rut','nombre','apellido','parentezco','direccion','telefono']   
        widgets={
            'rut':forms.TextInput(attrs={'placeholder':'Rut de la carga familiar','class':'form-control mt-2'}),
            'nombre':forms.TextInput(attrs={'placeholder':'Nombre de la carga familiar','class':'form-control mt-2'}),
            'apellido':forms.TextInput(attrs={'placeholder':'Apellido de la carga familiar','class':'form-control mt-2'}),
            'direccion':forms.TextInput(attrs={'placeholder':'Dirección de la carga familiar','class':'form-control mt-2'}),
            'telefono':forms.TextInput(attrs={'placeholder':'Teléfono de la carga familiar','class':'form-control mt-2'})

        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields ['parentezco'].widget.attrs.update({'class':'form-control mt-2'})

class LoginForm(forms.Form):
    correo = forms.CharField(label='Email',max_length=63, widget=forms.TextInput(attrs={'placeholder': 'Ingrese su correo','class':'form-control mt-2'}))
    password = forms.CharField(label='Contraseña',max_length=63, widget=forms.PasswordInput(attrs={'placeholder': 'Ingrese su contraseña','class':'form-control mt-2'}))

class modificarUserform(forms.ModelForm):
    class Meta:
        model=Usuario
        fields=['nombre','apellido','direccion','telefono']
        widgets={
            'nombre':forms.TextInput(attrs={'class':'form-control mt-2'}),
            'apellido':forms.TextInput(attrs={'class':'form-control mt-2'}),
            'direccion':forms.TextInput(attrs={'class':'form-control mt-2'}),
            'telefono':forms.TextInput(attrs={'class':'form-control mt-2'})
        }
   