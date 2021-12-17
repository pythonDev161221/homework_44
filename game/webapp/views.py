from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index_view(request):
    global context
    if request.method == "GET":
        context = {
            'answer': 'need to fill than there will be answer'
        }
        return render(request, 'index.html', context)
    elif request.method == 'POST':
        context = {}
        numbers = request.POST.get('num')
        numbers = numbers.split(" ")
        l = []
        for i in numbers:
            l.append(int(i))
        # print(l)

        context = {
            'answer': l
        }
    return render(request, "index.html", context)
