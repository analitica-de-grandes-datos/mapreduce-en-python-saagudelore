#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

file = sys.stdin

dictionary = {}
for line in file:
    key, val = line.split('\t')

    if key in dictionary:
        dictionary[key] += int(val)
    else:
        dictionary[key] = 1

print('\n'.join([f'{clave}\t{valor}' for clave, valor in dictionary.items()]))