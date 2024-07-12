from django import forms
from main.models import *

class formularioRegistro(forms.ModelForm):
    
    password= forms.CharField(label='Contraseña:', widget=forms.PasswordInput(attrs={'placeholder':'Ingrese su contraseña'}))
    password_2=forms.CharField(label='Repita la contraseña:', widget=forms.PasswordInput(attrs={'placeholder':'Re-ingrese su contraseña'}))
    rut = forms.CharField(label='Cedula de identidad del trabajador', widget=forms.TextInput(attrs={'placeholder':'Ingrese rut'})) #TUVE QUE PONER EL RUT AQUI PARA QUE NO ME DIERA ERROR
    class Meta:
        model= Usuario
        fields=['correo','rut','nombre','apellido','direccion','telefono','area_desempeno','cargo']
        widgets={
            'nombre': forms.TextInput(attrs={'placeholder':'Ingrese nombre'}), #Tuve que borrar los attr para que tambien mon diera error 
            'correo': forms.TextInput(attrs={'placeholder':'Ingrese email'}),
            'apellido': forms.TextInput(attrs={'placeholder':'Ingrese apellido'}),
            'direccion': forms.TextInput(attrs={'placeholder':'Ingrese la direccion'}),
            'telefono': forms.TextInput(attrs={'placeholder':'Ingrese telefono'}),
            'area_desempeno': forms.TextInput(attrs={'placeholder':'Ingrese lugar de trabajado'}),
            'cargo': forms.TextInput(attrs={'placeholder':'Escriba el cargo'}),
        }
        def clean_email(self):
            email= self.cleaned_data.get('correo')
            qs=Usuario.objects.filter(email=email)
            if qs.exists():
                raise forms.ValidationError("El correo ya esta en uso")
            return email

        def clean(self):
            cleaned_data=super().clean()
            password= cleaned_data.get("password")
            password_2=cleaned_data.get("password_2")
            rut = cleaned_data.get("rut")
            nombre=cleaned_data.get("nombre")
            apellido= cleaned_data.get("apellido")
            direccion= cleaned_data.get("direccion")
            telefono= cleaned_data.get("telefono")
            area_desempeno= cleaned_data.get("area_desempeno")
            cargo=cleaned_data.get("cargo")
            qs=Usuario.objects.filter(rut=rut)
            if qs.exists:
                self.add_error("El rut ya esta registrado")
            if len(password)< 8:
                self.add_error("La contraseña debe ser mayor a 8 digitos")
            if password is not None and password !=password_2:
                self.add_error("Las contraseñas no coinciden")
            if nombre is None:
                self.add_error("Debe rellenar este campo")
            if apellido is None:
                self.add_error("Debe rellenar este campo")
            if direccion is None:
                self.add_error("Debe rellenar este campo")
            if telefono is None:
                self.add_error("Debe rellenar este campo")
            if area_desempeno is None:
                self.add_error("Debe rellenar este campo")
            if cargo is None:
                self.add_error("Debe rellenar este campo")
            return cleaned_data

class BusquedaTrabajadorForm(forms.Form):
    rut = forms.CharField(label='Ingrese el Rut del trabajador', max_length=12)