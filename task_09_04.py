def my_decorator(func):
    def do_some_staff(a, b, c):
        return func(c, b, a)
    return do_some_staff


@my_decorator
def my_func(a, b, c):
    print(f'first - {a}, second - {b}, third - {c}')


my_func(1, 2, 3)
