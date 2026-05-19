from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {
            'username': 'Имя пользователя',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'email': 'Email',
        }


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['patronymic', 'phone', 'telegram_id']
        labels = {
            'patronymic': 'Отчество',
            'phone': 'Телефон',
            'telegram_id': 'Telegram ID',
        }


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = "Имя пользователя:"
        self.fields['username'].help_text = "Обязательно.\nНе более 150 символов. Только буквы, цифры и @/./+/-/_."
        self.fields['password1'].label = "Пароль:"
        self.fields['password1'].help_text = "Не должен быть слишком похож на вашу другую личную" \
                                             "информацию.\n"\
                                             "Должен содержать не менее 8 символов.\n" \
                                             "Не может быть общеупотребимым паролем.\n" \
                                             "Не может состоять только из цифр.\n"
        self.fields['password2'].label = "Подтверждение пароля:"
        self.fields['password2'].help_text = "Введите тот же пароль, что и раньше, для проверки."