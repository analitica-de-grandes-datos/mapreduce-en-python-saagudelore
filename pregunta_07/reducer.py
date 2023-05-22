#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

file = sys.stdin
dictionary = {}

for line in file:
    key, date, val = line.strip().split('\t')
    val = int(val)
    if key in dictionary:
        dictionary[key].append([date, val])
    else:
        dictionary[key] = [[date, val]]

for letter in dictionary:
    dictionary[letter] = sorted(dictionary[letter], key=lambda x: x[1])
    for lista in dictionary[letter]:
        print(f'{letter}   {lista[0]}   {lista[1]}')