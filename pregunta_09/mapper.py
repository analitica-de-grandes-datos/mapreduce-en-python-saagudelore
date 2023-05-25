#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

file = sys.stdin

for line in file:
    letter, date, number = line.strip().split('   ')
    print(f'{letter}\t{date}\t{number}')