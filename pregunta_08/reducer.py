#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

file = sys.stdin
dictionary = {}

for line in file:
    letter, number = line.strip().split('\t')
    number = float(number)

    if letter in dictionary:
        dictionary[letter][0] += number
        dictionary[letter][1] += 1
    else:
        dictionary[letter] = [number, 1]


print('\n'.join([f'{clave}\t{valor[0]}\t{valor[0]/valor[1]}' for clave, valor in dictionary.items()]))
