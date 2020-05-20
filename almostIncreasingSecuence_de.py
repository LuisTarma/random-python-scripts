def primer_par(sequence, k):
    """Devuelve el primer indice de un par de elementos en la secuencia[]
    para indices k-1, k+1, k+2, k+3, ... donde el elemento anterior es
    no menor que el elemento posterior. Si no existe ese par, devuelve -1. """
    if 0 < k < len(sequence) - 1:
        if sequence[k-1] >= sequence[k+1]:
            return k-1
    for i in range(k+1, len(sequence)-1):
        if sequence[i] >= sequence[i+1]:
            return i
    return -1

def almostIncreasingSequence(sequence):
    j = primer_par(sequence, -1)
    if j == -1:
        return True #La lista esta aumentando
    if primer_par(sequence, j) == -1:
        return True  # Eliminando el elemento anterior la lista aumenta
    if primer_par(sequence, j+1) == -1:
        return True  # Eliminando el elemento posterior la lista aumenta
    return False 
    
