from django import forms

from django.contrib.auth.models import User

# ()   {}  <!--  -->
class RegisterForm(forms.Form):
    
    #Para trabajar con estilos va ser necesario usar el atributo widget
    username=forms.CharField(required=True,
                             min_length=4,
                             max_length=50,
                             widget=forms.TextInput(attrs={
                                 'class' : 'form-control',
                                 'id':'username'
                             } ))   
    email=forms.EmailField(required=True,
                           max_length=30,
                            widget=forms.EmailInput(attrs={
                            'class' : 'form-control',
                            'id':'email',
                            'placeholder':'example@gmail.com'
                             } )) 
    password=forms.CharField(required=True,
                             max_length=30,
                            widget=forms.PasswordInput(attrs={
                            'class' : 'form-control',
                            'id':'password'
                             } )) 
    
    
    #vamos a validar ahora los campos
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            #raise - se usa para generar una excepcion intencional
            #Con esto vamos a mostrar los errores
            raise forms.ValidationError('El username ya se encuentra en uso')
            #print('El usuario {} se encuentra duplicado'.format(username))
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            #raise - se usa para generar una excepcion intencional
            raise forms.ValidationError('El email ya se encuentra en uso')
            #print('El usuario {} se encuentra duplicado'.format(username))
        return email