#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

file = sys.stdin

for line in file:
    words = line.strip().split('   ')
    letter, value = words[0], words[2]
    print(f'{letter}\t{value}')