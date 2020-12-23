from utilities import *
import pycosat

if __name__ == '__main__':

    N = 9
    M = 3
    cnf = []

    # Cell, row and column constraints
    for i in range(N):
        for s in range(N):
            cnf = cnf + exactly_one([transform(i, j, s, N) for j in range(N)])
            cnf = cnf + exactly_one([transform(j, i, s, N) for j in range(N)])

        for j in range(N):
            cnf = cnf + exactly_one([transform(i, j, k, N) for k in range(N)])

    # Sub-matrix constraints
    for k in range(N):
        for x in range(M):
            for y in range(M):
                v = [transform(y * M + i, x * M + j, k, N) for i in range(M) for j in range(M)]
                cnf = cnf + exactly_one(v)

    # See contribution from @GregoryMorse below
    cnf = {frozenset(x) for x in cnf}
    cnf = list(cnf)

    # A 16-constraint Sudoku

    constains2 = [
        (1, 4, 2),
        (1, 5, 6),
        (1, 7, 7),
        (1, 9, 1),
        (2, 1, 6),
        (2, 2, 8),
        (2, 5, 7),
        (2, 8, 9),
        (3, 1, 1),
        (3, 2, 9),
        (3, 6, 4),
        (3, 7, 5),
        (4, 1, 8),
        (4, 2, 2),
        (4, 4, 1),
        (4, 8, 4),
        (5, 3, 4),
        (5, 4, 6),
        (5, 6, 2),
        (5, 7, 9),
        (6, 2, 5),
        (6, 6, 3),
        (6, 8, 2),
        (6, 9, 8),
        (7, 3, 9),
        (7, 4, 3),
        (7, 8, 7),
        (7, 9, 4),
        (8, 2, 4),
        (8, 5, 5),
        (8, 8, 3),
        (8, 9, 6),
        (9, 1, 7),
        (9, 3, 3),
        (9, 5, 1),
        (9, 6, 8)
    ]
    constraints = [(x[0] - 1, x[1] - 1, x[2]) for x in constains2]

    cnf = cnf + [[transform(z[0], z[1], z[2]) - 1, N] for z in constraints]
    dict_s = {}
    for x in constraints:
        dict_s[(x[0] + 1) * (x[1] + 1)] = x[2]

    for solution in pycosat.itersolve(cnf):
        X = [inverse_transform(v, N) for v in solution if v > 0]
        for i, cell in enumerate(sorted(X, key=lambda h: h[0] * N * N + h[1] * N)):
            if i + 1 % M == 0:
                print("|", end=" ")

            print(cell[2] + 1, end=" ")
            if (i + 1) % N == 0: print("")
