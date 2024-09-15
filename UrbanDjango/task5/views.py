from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister


# Create your views here.
def sign_up_by_html(request):
    users = ['user1', 'user2', 'user3']
    info = {}
    context = {
        'info': info
    }
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        if username not in users and password == repeat_password and int(age) >= 18:
            return HttpResponse(f'Приветствуем, {username}!')
        else:
            if username in users:
                info['error'] = 'Пользователь уже существует'
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
    return render(request, 'fifth_task/registration_page.html', context)


def sign_up_by_django(request):
    users = ['user1', 'user2', 'user3']
    info = {}
    context = {
        'info': info
    }
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if username not in users and password == repeat_password and age >= 18:
                return HttpResponse(f'Приветствуем, {username}!')
            else:
                if username in users:
                    info['error'] = 'Пользователь уже существует'
                elif password != repeat_password:
                    info['error'] = 'Пароли не совпадают'
                elif age < 18:
                    info['error'] = 'Вы должны быть старше 18'
    else:
        form = UserRegister()
    return render(request, 'fifth_task/registration_page.html', {'form': form, 'info': info})
