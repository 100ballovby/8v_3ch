'''Написать программу, которая называет день недели по его порядковому номеру'''

days = {
    1: 'monday',
    2: 'tuesday',
    3: 'wednesday ',
    4: 'thursday',
    5: 'friday',
    6: 'saturday',
    7: 'sunday'
}  # словарь (пары ключ:значение)

n = int(input('Введите номер дня недели: '))
if 1 <= n <= 7:
    print(days[n])
else:
    print('Введите число от 1 до 7')

