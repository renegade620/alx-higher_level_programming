#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

   def print_matrix_integer(matrix=[[]]):
    if matrix:
        for row in matrix:
            x = len(row)
            for i in range(x):
                print("{:d}".format(row[i]), end=" " if i < x -1 else "")
            print()    
