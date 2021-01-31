def func(**kwargs):
    for key, value in kwargs.items():
        if len(key) % 2 == 0:
            print(f'{key}:\'{value}\'')


func(aaaa=4,bbbbb=4,aa=3,bbb=3,erwr=4)
