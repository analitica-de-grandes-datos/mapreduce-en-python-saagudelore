#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

file = sys.stdin
dictionary = {}

for line in file:
    letter, val = line.strip().split('\t')
    val = float(val)

    if letter in dictionary:
        dictionary[letter] = [max(val,dictionary[letter][0]), min(val,dictionary[letter][1])]
    else:
        dictionary[letter] = [val, val]

print('\n'.join([f'{clave}\t{valor[0]}\t{valor[1]}' for clave, valor in dictionary.items()]))