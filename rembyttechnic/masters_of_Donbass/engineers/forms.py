from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Engineer
from django.forms import ModelForm


class EngineerForm(ModelForm):
    class Meta:
        model = Engineer
        fields = ['name', 'email', 'username', 'i_info', 'all_info', 'engineer_image', 'education', 'price',
                  'social_website', 'social_whatsapp', 'social_telegram']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({'class': 'input'})

class EngineerUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {'first_name': 'Имя инженера'}  # переопределяем название первого поля в форме регистрации

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({'class': 'input'})

