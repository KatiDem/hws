##Создать декоратор для функции, которая принимает список чисел.
##Декоратор должен производить предварительную проверку данных -
##удалять все четные элементы из списка.

def my_decorator(func):
    def do_some_staff():
        result_list = list(filter(lambda x: x % 2 == 1, list(func())))
        print(result_list)
        return func()
    return do_some_staff


@my_decorator
def my_func():
    result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 81, 54, 93, 11]
    return result


my_func()
