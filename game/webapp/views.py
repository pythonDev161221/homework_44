from random import randint
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def num_list_create(N):
    list_num = []
    for i in range(N):
        while True:
            a = randint(1, 9)
            if a not in secret_nums:
                list_num.append(a)
                break
    return list_num

def index_view(request):
    global secret_nums, context, N
    if request.method == "GET":
        N = 4
        secret_nums = []
        secret_nums = num_list_create(N)

        context = {
            'answer': 'need to fill than there will be answer',
            'secret_nums': secret_nums,
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
        except ValueError:
            context['answer'] = 'it is need to input only numbers'
            return render(request, 'index.html', context)
        n = num_list
        if len(n) != N:
            context['answer'] = f'it should be {N} numbers'
            return render(request, 'index.html', context)
        for i in n:
            if i > 9 or i < 1:
                context['answer'] = 'value should be between 1 and 9 included'
                return render(request, 'index.html', context)
            elif n.count(i) > 1:
                context['answer'] = 'any number should not repeated twice or more'
                return render(request, 'index.html', context)




        context = {
            'answer': n,
            'secret_nums': secret_nums,
        }
    return render(request, "index.html", context)
