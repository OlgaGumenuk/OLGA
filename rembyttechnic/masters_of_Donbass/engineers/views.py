from django.shortcuts import render
from .models import Engineer

def engineers(request):
    engi = Engineer.objects.all()
    context = {'engineers': engi}
    return render(request, 'engineers/index.html', context)

def file_engineer(request, pk):
    engi = Engineer.objects.get(id=pk)
    context = {'engineer': engi}
    return render(request, 'engineers/file_engineer.html', context)

