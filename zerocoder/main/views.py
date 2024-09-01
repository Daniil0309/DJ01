from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index_view(request):
    return HttpResponse("This is the index page.")
def data_view(request):
    return HttpResponse("<h1>Это data</h1>")

def test_view(request):
    return HttpResponse("<h1>Это test</h1>")
