array = ['h', 'e', 'l', 'l', 'o', [4565, 23], 32]
string = 'hello'

# print(array[5])
# print(string[1])

''''''
phrase = input('Введите фразу: ')
owl = ''
for letter in phrase:
    if letter not in 'аеиоуыэюя ':
        owl += letter
print(owl)
