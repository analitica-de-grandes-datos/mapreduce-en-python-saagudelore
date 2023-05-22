#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#

# Emparejar entradas como (clave, valor)

import sys

file = sys.stdin

for line in file:
    words = line.split(',')
    credit_history = words[2]
    print(f"{credit_history}\t1")