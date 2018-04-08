# from django.core.cache import cache
# from fiboapp.models import FibbonaciNumbers


def memoize(f):
    cache = {}

    def decorated_function(*args):
        if args in cache:
            return cache.get(args)
        else:
            cache.set(args, f(*args))
            return cache.get(args)
    return decorated_function


@memoize
def fib(n):
    return n if n < 2 else fib(n - 2) + fib(n - 1)


def fib_cache():
    for i in range(500, 500000, 500):
        fib(i)


# def update_fibo_table():
#     for i in range(500, 500000, 500):
#         FibbonaciNumbers.objects.get_or_create(n=i, value=fib(i))


if __name__ == "__main__":
    fib_cache()
