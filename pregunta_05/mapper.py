#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

file = sys.stdin

for line in file:
    words = line.strip().split('   ')
    date = words[1]
    month = date.split('-')[1]
    print(f'{month}\t1')
