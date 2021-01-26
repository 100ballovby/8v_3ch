'''
try:
    do_this
except:
    to_this
'''
n = int(input('Введите число: '))
d = int(input('Введите делитель: '))

try:
    res = n / d
    print(res)
except ZeroDivisionError:
    print('На 0 делить нельзя!')