from fiboapp.models import FibbonaciNumbers
from django.core.management.base import BaseCommand


def memoize(f):
    cache = {}

    def decorated_function(*args):
        if args in cache:
            return cache.get(args)
        else:
            cache[args] = f(*args)
            return cache.get(args)
    return decorated_function


@memoize
def fib(n):
    return n if n < 2 else fib(n - 2) + fib(n - 1)


def update_fibo_table():
    for i in range(500, 50000, 10):
        print(i)
        FibbonaciNumbers.objects.get_or_create(n=i, value=fib(i))
        FibbonaciNumbers.objects.get_or_create(n=i + 1, value=fib(i + 1))
        FibbonaciNumbers.objects.get_or_create(n=i + 2, value=fib(i + 2))
        FibbonaciNumbers.objects.get_or_create(n=i + 3, value=fib(i + 3))
        FibbonaciNumbers.objects.get_or_create(n=i + 4, value=fib(i + 4))
        FibbonaciNumbers.objects.get_or_create(n=i + 5, value=fib(i + 5))
        FibbonaciNumbers.objects.get_or_create(n=i + 6, value=fib(i + 6))
        FibbonaciNumbers.objects.get_or_create(n=i + 7, value=fib(i + 7))
        FibbonaciNumbers.objects.get_or_create(n=i + 8, value=fib(i + 8))
        FibbonaciNumbers.objects.get_or_create(n=i + 9, value=fib(i + 9))


class Command(BaseCommand):
    help = 'A description of your command'

    def handle(self, *args, **options):
        print('here')
        update_fibo_table()
