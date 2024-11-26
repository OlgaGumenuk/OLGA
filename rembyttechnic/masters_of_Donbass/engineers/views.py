from django.shortcuts import render, redirect
from .models import Engineer
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist  # для обработки исключений
from django.contrib.auth.decorators import login_required  # модуль-декоратор для ограничения видимостти неавторизо
# ванным пользователям функции добавить ремонт
from django.contrib import messages
from .forms import EngineerUserCreationForm, EngineerForm
from django.db.models import Q
from .utils import search_engineers, paginate_engineers


def engineers(request):
    engi, search_query = search_engineers(request)

    custom_range, engi = paginate_engineers(request, engi, 6)

    context = {
        'engineers': engi,
        'search_query': search_query,
        'custom_range': custom_range
    }
    return render(request, 'engineers/index.html', context)


def file_engineer(request, pk):
    engi = Engineer.objects.get(id=pk)
    context = {'engineer': engi}
    return render(request, 'engineers/file_engineer.html', context)


def login_engineer(request):
    if request.method == "POST":  # забираем данные кот. внес поль-ль
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)  # получаем данные по имени поль-ля(если есть учетная запись)
        except ObjectDoesNotExist:
            messages.error(request, "Такого пользователя не существует.")  # если нет учетн.записи то выдаст
            # исключение

        user = authenticate(request, username=username, password=password)  # это проверка существует ли в базе данных
        # такои поль-ль с паролем

        if user is not None:  # если user не является знанчением None
            login(request, user)  # то мы его авторизируем с пришедшим именем и паролем
            return redirect('engineers')  # перенаправляем
        else:
            messages.error(request, "Имя или пароль некорректны")

    return render(request, 'engineers/login_register.html')


def logout_engineer(request):
    logout(request)
    messages.info(request, "Пользователь вышел из учетной записи.")
    return redirect('login')


def register_engineer(request):
    page = 'register'
    form = EngineerUserCreationForm()

    if request.method == "POST":
        form = EngineerUserCreationForm(request.POST)  # собираем все поля из формы
        if form.is_valid():
            user = form.save(commit=False)  # сохранит и переведет в нижний регистр
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'Аккаунт пользователя успешно создан!')
            login(request, user)
            return redirect('engineers')
        else:
            messages.error(request, 'При регистрации произошла ошибка.')

    context = {'page': page,
               'form': form
               }
    return render(request, 'engineers/login_register.html', context)


@login_required(login_url='login')  # если зашел незареганный польль то перенаправим на авторизацию
def engineer_account(request):
    prof = request.user.engineer  # у текущего польля берем его данные
    # class2 = prof.class2_set.all()  # если бы была обратная связь со 2-ой таблицей данных
    repairs = prof.repair_set.all()
    context = {
        'profile': prof,
        'repairs': repairs
    }  # текущего польля
    return render(request, 'engineers/account.html', context)


@login_required(login_url='login')
def edit_account(request):
    engineer = request.user.engineer
    form = EngineerForm(instance=engineer)  # instance= будет инфа из бд об этом польле в ячейках формы

    if request.method == "POST":
        form = EngineerForm(request.POST, request.FILES, instance=engineer)  # забрираем все
        # текстовые & FILES - поля  и что из имеющейся уже модели берем
        if form.is_valid():
            form.save()
            return redirect('account')

    context = {
        'form': form
    }
    return render(request, 'engineers/engineer_form.html', context)
