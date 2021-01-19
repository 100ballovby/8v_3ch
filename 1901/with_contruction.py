#with open('example.txt', 'w') as f:
#    f.write('Привет!')

#with open('example.txt', 'r') as f:
#    for line in f:
#        print(line)

list_of_phrases = [
    'привет андрей\n',
    'а я сяду в кабриолет\n',
    'и уеду куда-нибудь\n',
    'если вспомнишь меня  - забудь\n',
    'А вернешься - меня здесь нет\n',
    'а я сяду в кабриолет\n'
]
with open('example.txt', 'w') as f:
    f.writelines(list_of_phrases)