from django.shortcuts import render
from .tasks import text


def index(request):
    text.delay()
    return render(request, 'index.html')