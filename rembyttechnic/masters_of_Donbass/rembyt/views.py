from django.shortcuts import render, redirect
from .models import Repair
from .forms import RepairForm


def repairs(request):
    rep = Repair.objects.all()
    context = {'repairs': rep}
    return render(request, "rembyt/repairs.html", context)


def repair(request, pk):
    repair_obj = Repair.objects.get(id=pk)
    context = {'repair': repair_obj}
    return render(request, "rembyt/single-repair.html", context)

def create_repair(request):
    form = RepairForm()

    if request.method == "POST":
        form = RepairForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('repairs')

    context = {'form': form}
    return render(request, 'rembyt/form-create.html', context)

