from django.shortcuts import render

# Create your views here.

def index(request):
    template = 'index.html'
    return render(request, template)
    
def auth_return(request):
    template = '404.html'
    return render(request, template)
