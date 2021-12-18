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
            'answer': 'Заполните пустую строку и ответ будет здесь',
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
            context['answer'] = 'нужно вводить только числа'
            return render(request, 'index.html', context)
        n = num_list

        if len(n) != N:
            context['answer'] = f'Должно быть {N} числа'
            return render(request, 'index.html', context)
        for i in n:
            if i > 9 or i < 1:
                context['answer'] = 'значение доолжно быть от 1 до 9-ти'
                return render(request, 'index.html', context)
            elif n.count(i) > 1:
                context['answer'] = 'числа не должны повторяться'
                return render(request, 'index.html', context)

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
            ans = f'количество Быков: {b}; и количество Коров: {c}'
        nums_history.append(ans)
        context = {
            'answer': ans,
            'secret_nums': secret_nums,
            'client_nums': n,
        }
    return render(request, "index.html", context)


def nums_history_view(request):
    context_nums = {}
    dict_nums = {}
    for i in range(len(nums_history)):
        dict_nums[i+1] = nums_history[i]
    context_nums['nums'] = dict_nums
    return render(request, 'history.html', context_nums)
