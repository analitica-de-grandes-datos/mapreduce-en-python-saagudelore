#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

file = sys.stdin
dictionary = {}

for line in file:
    month = line.strip().split('\t')[0]
    if month in dictionary:
        dictionary[month] += 1
    else:
        dictionary[month] = 1

print('\n'.join([f'{clave}\t{valor}' for clave, valor in dictionary.items()]))
