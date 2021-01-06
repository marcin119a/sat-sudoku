from utilities import *
import pycosat



def sat_sudoku(N, M, constraints):
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



    cnf = cnf + [[transform(z[0], z[1], z[2] - 1, N)] for z in constraints]
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
    