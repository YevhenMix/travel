from django.shortcuts import render


def home(request):
    print(request.path)
    return render(request, 'base.html')
