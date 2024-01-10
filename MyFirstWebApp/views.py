from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    print('hi')
    return render(request, 'index.html')
