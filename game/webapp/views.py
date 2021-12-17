from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index_view(request):
    if request.method == "GET":
        return render(request, 'index.html')
    elif request.method == 'POST':
        context = {}
        numbers = request.POST.get('numbers')
        print(numbers)
        print(numbers)
        print(numbers)

    return render(request, 'index.html')
