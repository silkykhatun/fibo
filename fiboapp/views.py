import json
import time
from django.shortcuts import render
from fiboapp.models import FibbonaciNumbers
from fiboapp.management.commands.update_fibo_table import fib
from django.http import JsonResponse
# Create your views here.


def index(request):
    return render(request, template_name='index.html')


def get_fibo(request):
    t1 = time.time()
    try:
        n = int(request.GET.get('number'))
    except Exception as e:
        print(e)
        n = None
    val = get_fib(n)
    t2 = time.time()
    return JsonResponse({'data': val, 'time': (t2 - t1) * 1000}, content_type="application/json")


def get_fib(n):
    if n > 50000:
        raise Exception('Number too high!')
    elif n < 500:
        return {'key': n, 'value': str(fib(n))}
    else:
        try:
            f = FibbonaciNumbers.objects.get(n=n)
            return {'key': n, 'value': f.value}
        except:
            return {'key': n, 'value': str(fib(n))}
