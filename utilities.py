def exactly_one(variables):
    cnf = [ variables ]
    n = len(variables)

    for i in range(n):
        for j in range(i+1, n):
            v1 = variables[i]
            v2 = variables[j]
            cnf.append([-v1, -v2])

    return cnf


def transform(i, j, k):
    return i*N*N + j*N + k + 1


def inverse_transform(v):
    v, k = divmod(v-1, N)
    v, j = divmod(v, N)
    v, i = divmod(v, N)
    return i, j, k