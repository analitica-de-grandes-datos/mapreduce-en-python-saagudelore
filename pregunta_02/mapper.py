#
# >>> Escriba el codigo del mapper a partir de este punto <<<
# 
import sys

file = sys.stdin

for line in file:
    words = line.split(',')
    purpose, amount = words[3], words[4]
    print(f"{purpose}\t{amount}")