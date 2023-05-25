#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

file = sys.stdin

n = 5
lista = []

for line in file:
    letter, date, value = line.strip().split('\t')
    value = int(value)
    lista.append([f'{letter}   {date}   {value}', value])
    
lista_n = sorted(lista, key=lambda x: x[1])[:6]
for val in lista_n:
    print(val[0])

