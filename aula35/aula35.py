# def func (arg, arg2):
#     return arg * arg2
#
# var = func(2,2)
# print(var)

# def func (arg, arg2):
#     return arg * arg2
#
# var = func(2,2)

lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8],
]

lista.sort(key=lambda i:i[1])

print(lista)