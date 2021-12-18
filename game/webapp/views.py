from random import randint
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def num_list_create(n):
    list_num = []
    for i in range(n):
        while True:
            a = randint(1, 9)
            if a not in list_num:
                list_num.append(a)
                break
    return list_num


def index_view(request):

    global secret_nums, context, N, nums_history

    if request.method == "GET":
        nums_history = []
        N = 4
        secret_nums = []
        secret_nums = num_list_create(N)

        context = {
            'answer': 'fill input and there will be a result',
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
        nums_history.append(n)
        b = 0
        c = 0
        for i in n:
            for j in secret_nums:
                if i == j:
                    if n.index(i) == secret_nums.index(j):
                        b += 1
                    else:
                        c += 1
        if b == N:
            ans = 'Congratulation. You win!!!'
        else:
            ans = f'bulls is: {b}; and cows is: {c}'

        context = {
            'answer': ans,
            'secret_nums': secret_nums,
            'client_nums': n,
            'nums_history': nums_history,

        }
    return render(request, "index.html", context)


def nums_history_view(request):
    # context_nums = {}
    # for i in nums_his:
    #     context_nums[nums_his.index(i)] = i
    return render(request, 'history.html')
