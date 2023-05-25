#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

file = sys.stdin

dictionary = {}
for line in file:
    letter, value = line.strip().split('\t')
    if letter in dictionary:
        dictionary[letter] += f',{value}'
    else:
        dictionary[letter] = value

for clave in dictionary:
    lista = [int(x) for x in dictionary[clave].split(",")]
    lista = sorted(lista)
    dictionary[clave] = ''
    for letter in lista:
        if dictionary[clave] == '':
            dictionary[clave] += f'{letter}'
        else:
            dictionary[clave] += f',{letter}'
    print(f'{clave}\t{dictionary[clave]}')