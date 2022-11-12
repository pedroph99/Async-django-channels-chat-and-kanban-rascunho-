from xml.dom import ValidationErr
from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
class NameForm(forms.Form):
    usuario = forms.CharField(label='Your name', max_length=100)
    senha = forms.CharField(label='Your name', max_length=100)
    def clean_usuario(self):
        print('entrei')
        data = self.cleaned_data['usuario']
        usuarios = get_user_model()
        try: 
            usuarios.objects.get(username=data)
            print('Usuário existe')
            raise ValidationError('Usuário já existe')
        except:
            return data