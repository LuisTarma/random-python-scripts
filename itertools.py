
from itertools import *

# Funcion cycle(lista o cadena)
"""
contador = 0
for elemento in cycle([10, 12, 14]):
    print(elemento, end = ' ')
    contador += 1
    if contador == 20:
        break
"""
# Funcion count(inicio, paso)
for valor in count(5, 3):
    print(valor, end = ' ')
    if valor == 20:
        break

# Funcion repeat(objeto_a_repetir, numero_de_veces)
for elemento in repeat(3, 5):
    print(elemento, end = ' ')
