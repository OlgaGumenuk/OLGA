from django.shortcuts import render, redirect
from .models import Repair
from .forms import RepairForm
from django.contrib.auth.decorators import login_required  # модуль-декоратор для ограничения видимостти неавторизо
# ванным пользователям функции добавить ремонт
from django.db.models import Q
from .utils import search_repair, paginate_repairs



def repairs(request):
    rep, search_query2 = search_repair(request)

    custom_range, rep = paginate_repairs(request, rep, 6)


    context = {
        'repairs': rep,
        'search_query2': search_query2,
        # 'paginator': paginator,
        'custom_range': custom_range
    }
    return render(request, "rembyt/repairs.html", context)


def repair(request, pk):
    repair_obj = Repair.objects.get(id=pk)
    context = {'repair': repair_obj}
    return render(request, "rembyt/single-repair.html", context)


@login_required(login_url="login")  # это путь куда переходим если незареган поль-ль
def create_repair(request):
    engineer = request.user.engineer  # чтобы новый польль смог запонить на себя форму
    form = RepairForm()

    if request.method == "POST":  # сохранение данных при нажатии submit или записать
        form = RepairForm(request.POST, request.FILES)
        if form.is_valid():
            repair = form.save(commit=False)
              # отменяем загрузку в базу данных чтобы новый польль смог запонить на себя форму
            repair.owner = engineer  # присвоим собственнику ремонта его данные из класса engineer
            repair.save()
            return redirect('account')

    context = {'form': form}
    return render(request, 'rembyt/form-create.html', context)


@login_required(login_url="login")
def update_repair(request, pk):
    engineer = request.user.engineer  # получили доступ к модели engineer, берутся данные авторизованного польля
    repair = engineer.repair_set.get(id=pk)  # т.к.нет прямого доступа от engineer к repair есть только обратная связь
    form = RepairForm(instance=repair)

    if request.method == "POST":  # сохранение данных при нажатии submit или записать
        form = RepairForm(request.POST, request.FILES, instance=repair)
        if form.is_valid():
            form.save()
            return redirect('account')

    context = {
        'repair': repair,
        'form': form
    }
    return render(request, 'rembyt/form-create.html', context)


@login_required(login_url="login")
def delete_repair(request, pk):
    engineer = request.user.engineer
    repair = engineer.repair_set.get(id=pk)

    if request.method == "POST":
        repair.delete()
        return redirect('account')

    context = {
        'object': repair
    }
    return render(request, 'rembyt/delete.html', context)