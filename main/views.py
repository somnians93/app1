from django.http import HttpResponse
from django.shortcuts import render

def index(request) -> HttpResponse:
    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели МебельHome',
    }
    return render(request, 'main/index.html', context)

def about(request) -> HttpResponse:
    context = {
        'title': 'МебельHome - О нас',
        'content': 'О нас',
        'text_on_page': 'У нас вы найдете все, что нужно для создания уюта и комфорта в вашем доме.'
    }
    return render(request, 'main/about.html', context)