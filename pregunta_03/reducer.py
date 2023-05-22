#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

file = sys.stdin
dictionary = {}

for line in file:
    key, val = line.strip().split('\t')
    dictionary[key] = int(val)

print('\n'.join([f'{clave},{valor}' for clave, valor in sorted(dictionary.items(), key=lambda x: x[1])]))