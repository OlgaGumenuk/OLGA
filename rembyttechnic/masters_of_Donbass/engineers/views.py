from django.shortcuts import render


def engineers(request):
    return render(request, 'engineers/index.html')
