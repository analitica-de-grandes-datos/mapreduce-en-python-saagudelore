#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

file = sys.stdin

for line in file:
    val, letters = line.strip().split('\t')
    letters = letters.split(',')
    for letter in letters:
        print(f'{letter}\t{val}')