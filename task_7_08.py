def arifm(args):
    summary = 0
    n = len(args)
    for i in args:
        summary += i
    return summary / n


def geomet(args):
    summary = 1
    n = len(args)
    for i in args:
        summary *= i
    return pow(summary, 1/n)


def srednee(*args, mean_type):
    if mean_type == 'arifmet':
        return arifm(args)
    elif mean_type == 'geometrich':
        return geomet(args)


### test ###

print(srednee(1, 2, 3, 4, 5, 4, 3, mean_type='arifmet'))
print(srednee(1, 2, 3, 4, 5, 4, 3, mean_type='geometrich'))
