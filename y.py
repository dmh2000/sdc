x = [1, 2, 3]
print(x)
print(*x)


def e(*args):
    print(args)


def f(**kwargs):
    print(kwargs)


f(a=1, b=2)
e([1, 2, 3], 4)
