

def matrixElementsSum(matrix):
    indice = 0
    su = 0
    for f in matrix:
        while indice != len(f):
            if f[indice] == 0:
                matrix = borrarCol(matrix, indice)
                indice = 0
                continue
            elif not f[indice] < 0:
                su += f[indice]
                f[indice] = -1
            indice += 1
        indice = 0
    return su


def borrarCol(matrix, i):
    for f in matrix:
        f.pop(i)
    return matrix

matrix = [[1, 1, 1, 0],
          [0, 5, 0, 1],
          [2, 2, 3, 3]]

def matrixElementsSuma(matrix):
    mt = list(zip(*matrix))
    print(mt)
    from itertools import takewhile
    return sum([sum(takewhile(lambda x: x > 0, y)) for y in mt])

print(matrixElementsSuma(matrix))


"""
After they became famous, the CodeBots all decided to move to a new building and live together.
The building is represented by a rectangular matrix of rooms. Each cell in the matrix contains
an integer that represents the price of the room. Some rooms are free (their cost is 0), but
that's probably because they are haunted, so all the bots are afraid of them. That is why any
room that is free or is located anywhere below a free room in the same column is not considered
suitable for the bots to live in.
Help the bots calculate the total price of all the rooms that are suitable for them.
"""