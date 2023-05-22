#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

file = sys.stdin

for line in file:
    words = line.strip().split('   ')
    letter, date, val = words[0], words[1], words[2]
    print(f'{letter}\t{date}\t{val}')