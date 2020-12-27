import numpy as np 

def exactly_one(variables):
    cnf = [ variables ]
    n = len(variables)

    for i in range(n):
        for j in range(i+1, n):
            v1 = variables[i]
            v2 = variables[j]
            cnf.append([-v1, -v2])

    return cnf


def transform(i, j, k, N):
    return i*N*N + j*N + k + 1


def inverse_transform(v, N):
    v, k = divmod(v-1, N)
    v, j = divmod(v, N)
    v, i = divmod(v, N)
    return i, j, k

def readSudoku(fileName):
    """
    Reads a Sudoku grid from a text file
    Empty cells are presented by 0
    Convert to internal format where empty cells are -1
    """
    
    data = np.loadtxt(fileName, skiprows=0, delimiter=" ", dtype=np.int);
    
    n = data.shape[0]
    return (data - np.ones([n, n], dtype=np.int))

def mapToConstrains(array):
    constrains = []
    print(array)
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i,j] != -1:
                constrains.append((i+1,j+1, array[i,j]+1))
    
    return constrains