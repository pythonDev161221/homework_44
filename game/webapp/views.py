from random import randint
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index_view(request):
    global hid_num, context
    if request.method == "GET":
        hid_num = []
        for i in range(4):
            hid_num.append(randint(1, 10))
        context = {
            'answer': 'need to fill than there will be answer',
            'hid_num': hid_num,
        }
        return render(request, 'index.html', context)
    elif request.method == 'POST':

        numbers = request.POST.get('num').strip()

        numbers = numbers.split(" ")

        num_list = []
        try:
            for i in numbers:
                if i:
                    num_list.append(int(i))
        except:
            context['answer'] = 'it is need to input only numbers'
            return render(request, 'index.html', context)

        context = {
            'answer': num_list,
            'hid_num': hid_num,
        }
    return render(request, "index.html", context)
