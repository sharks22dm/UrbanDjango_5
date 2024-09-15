from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'third_task/home.html')


def shop(request):
    return render(request, 'third_task/shop.html')


def basket(request):
    return render(request, 'third_task/basket.html')
