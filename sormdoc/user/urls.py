from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from . import views


app_name = 'user'

urlpatterns = [

    # Регистрация
    path('signup/', CreateView.as_view(
        template_name = 'user/signup.html',
        form_class = CustomUserCreationForm,
        success_url = reverse_lazy('user:login')
    ), name='signup'),

    # Смена пароля
    path('password_change/', auth_views.PasswordChangeView.as_view(
        template_name='registration/password_change_form.html',
        success_url='done/'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='password_change_done'),

    # Сброс пароля
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),

    # Вход
    path("login/", auth_views.LoginView.as_view(template_name='user/login.html'), name="login"),

    # Выход
    path('logout/', auth_views.LogoutView.as_view(next_page='user:login'), name='logout'),

    # Страница профиля
    path('profile/', views.profile, name='profile'),

]