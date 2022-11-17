from django.urls import path
from django.contrib.auth import views
from django.urls import reverse_lazy
from .views import *

app_name='secure'
urlpatterns = [
    path('',homeView,name='homeView'),
    path('dashboard/',dashboardView,name='dashboardView'),
    path('register/user/',registerView,name='registerView'),
    path('logout/user/',logoutView,name='logoutView'),
    path('account/locked/',accountLockView,name='accountLockView'),
    
    #1 - Submit our email form for change user password
    path('reset_password',views.PasswordResetView.as_view(template_name='passsword-reset/password-reset.html',success_url=reverse_lazy('secure:password_reset_done')),name='reset_password'),#A view for displaying a form and rendering a template response.
    
    #2 - A success message stating that an email was sent to reset our password
    path('reset_password_sent',views.PasswordResetDoneView.as_view(template_name='passsword-reset/password-reset-send.html'),name='password_reset_done'),#Render a template. Pass keyword arguments from the URLconf to the context.
    
    #3 - Send a link to our email... so that we can reset our password
    path('reset/<uidb64>/<token>/',views.PasswordResetConfirmView.as_view(template_name='passsword-reset/password-reset-form.html',success_url=reverse_lazy('secure:password_reset_complete')),name='password_reset_confirm'),#A view for displaying a form and rendering a template response.
    
    #4 - Show a success message stating that our password has was changed
    path('reset_password_complete',views.PasswordResetCompleteView.as_view(template_name='passsword-reset/password-reset-complete.html'),name='password_reset_complete')#Compling change password process successfully
    
]
