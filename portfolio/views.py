from django.shortcuts import render
from portfolio.models import Port

# Create your views here.
def home(request):
    portfolio = Port.objects.all()
        
    return render(request, 'pages/index.html', {'portfolio' : portfolio})
