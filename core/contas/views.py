import re

from django.contrib.auth.models import User
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string

from .models import Perfil
from .usuario_form import PerfilForm, UserForm


def validou_email(email):

    regex = '^(\w+)@[a-z]+(\.[a-z]+){1,2}$'

    if re.search(regex, email):
        return True

    return False


@transaction.atomic
def criar_conta(request):
    if request.method == 'POST':

        user = UserForm(request.POST)
        perfil = PerfilForm(request.POST, request.FILES)

        if perfil.is_valid() and user.is_valid():
            usr = User.objects.create_user(
                first_name=user.cleaned_data['first_name'],
                last_name=user.cleaned_data['last_name'],
                username=user.cleaned_data['username'],
                email=user.cleaned_data['email'],
                password=user.cleaned_data['password'],
            )

            perl = Perfil(
                bio=perfil.cleaned_data['bio'],
                foto=perfil.cleaned_data['foto'],
                user=usr,
            )

            perl.save()
            return redirect('login')
        return render(
            request,
            'contas/criar_conta.html',
            {'form': user, 'form_perfil': perfil},
        )
    return render(
        request,
        'contas/criar_conta.html',
        {'form': UserForm(), 'form_perfil': PerfilForm()},
    )


def htmx_valida_username(request):
    context = {
        'error_usrname': 'Username indisponível',
        'st_submit': 'disabled',
        'cor': 'red',
    }
    username_param = request.POST.get('username')

    if not User.objects.filter(username=username_param):
        context['error_usrname'] = 'Username disponível'
        context['cor'] = 'green'

    if PerfilForm(request.POST).is_valid():
        context['st_submit'] = ''

    str_template = render_to_string(
        'contas/feedback_form_validation.html', context
    )
    return HttpResponse(str_template)


def htmx_valida_senha(request):
    context = {
        'error_pwd': 'As senhas não coincidem',
        'st_submit': 'disabled',
        'cor': 'red',
    }
    pwd_confirm = request.POST.get('pwd_confirm')
    password = request.POST.get('password')

    if pwd_confirm == password and PerfilForm(request.POST).is_valid():
        context['error_pwd'] = ''
        context['st_submit'] = ''

    str_template = render_to_string(
        'contas/feedback_form_validation.html', context
    )
    return HttpResponse(str_template)


def htmx_valida_email(request):
    context = {'usr_email': '', 'st_submit': 'disabled', 'cor': 'red'}
    email = request.POST.get('email')

    if not validou_email(email):
        context['usr_email'] = 'Email inválido.'
    if User.objects.filter(email=email):
        context['usr_email'] = 'Email já se encontra cadastrado.'
    if PerfilForm(request.POST).is_valid():
        context['usr_email'] = ''
        context['st_submit'] = ''

    str_template = render_to_string(
        'contas/feedback_form_validation.html', context
    )
    return HttpResponse(str_template)
