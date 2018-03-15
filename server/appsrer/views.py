from django.shortcuts import render


# Create your views here.
def home(request):
    # return render(request, 'appeapi/index.html')
    return render(request, 'index.html')