from utilities import readSudoku, mapToConstrains
from sat_sudoku import sat_sudoku
import glob
import numpy as np
import math

if __name__ == "__main__":
    
    folder = "ShiDoku/"
    for filename in glob.glob(folder+"*.txt"):
        x = readSudoku(filename)
        n = int(math.sqrt(x.shape[0]))
        constains = mapToConstrains(x)
        sat_sudoku(n**2, n, constains)