from django.shortcuts import render


# Create your views here.
def menu(request):
    return render(request, 'fourth_task/menu.html')


def home(request):
    return render(request, 'fourth_task/home.html')


def shop(request):
    games = ['Atomic Heart', 'Cyberpunk 2077', 'PayDay 2']
    context = {
        'games': games
    }
    return render(request, 'fourth_task/shop.html', context)


def basket(request):
    return render(request, 'fourth_task/basket.html')
