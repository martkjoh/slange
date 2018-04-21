import numpy as np
import random
import time
from matplotlib import pyplot as plt
import copy
import sympy

def row_reduce(A):
    A
    i = 0
    while i < len(A): # Goes through the rows of the matrix
        for j in range(len(A[i])):  # Searches for the pivot. The number originally
            if not A[i][j]:         # stored in the pivot must be passed on to a
                continue
            else:
                pivot = j
                a = A[i][pivot]
                break
        for k in range(i, len(A[i])):  # Divides the whole row by the pivot
            A[i][k] = A[i][k] / a

        if not (i == len(A) - 1):           # This is to use the pivot to remove all numbers below
            for b in range(i + 1, len(A)):  # Goes thought all rows below the one we are working on
                x = -A[b][pivot]                # Sets of the number in the same column as the pivot, to set it to 0
                for c in range(i, len(A[b])):   # Goes trough the row, and subtracts the equation we are currently
                    A[b][c] += x*A[i][c]        # working on from (times the number below the pivot) from eq_c
            for f in range(pivot):              # Checks if there are any row with non-zero values to the
                if A[i + 1][f]:                 # to the left of the pivot
                    A[i + 1], A[i] = A[i], A[i + 1] # If so, they are switched, and the counter set back
                    i -= 2                      # Jumps back two values for now, but jumps forward onw before the end
        i += 1
    for i in range(len(A)): # Here, we are working upwards to set all numbers above pivots to 0
        #if sum(A[-i-1]):    # We skip all rows with just 0 (hoping it doesn't cancel out)
        for a in range(i + 1, len(A)): # This goes through all the pivots
            for b in range(len(A[0])): # This is to find the pivot
                if A[-a, b] != 0:
                    j = b - 1              # Saving the index of the pivot i a variable
                    break
            for b in range(a, len(A)):  # This goes trhtough all the numbers above the pivot
                x = -A[-b - 1, j]       # Sets x = the number above the pivot
                for c in range(len(A[0])):  # Goes though all numbers on the row
                    A[-b-1, c] += x*A[-a, c] # Subs the current pivot row * x from the numbers in the row
    return A


def det_rec(A):
    if np.shape(A) == (1, 1):
        return A
    else:
        D = 0
        for i, k in enumerate(A[0]):
            D += k * det_rec(np.concatenate(((A[1:][..., 0:i]).T, (A[1:][..., i+1:]).T)).T) * (-1)**i
        return D


def det_grahmshcmidt(A, return_mat=False):
    B = np.zeros_like(A)
    def proj(v, u):
        return sum(u * v) / sum(u * u) * u

    def orthogonolize(A, v):
        if np.shape(A) == (1, len(A[0])):
            return v - proj(v, A[-1])
        else:
            return orthogonolize(A[:-1], v - proj(v, A[-1]))

    for i in range(1, len(A)):
        B[i] = orthogonolize(A[:i], A[i])
    
    det = np.prod([np.sqrt(sum(u * u)) for u in A])
    
    if return_mat:
        return det, B 
    
    else:
        return det


def print_mat(A):
    x = ""
    for a in A:
        x += "["
        for b in a:
            if b >= 0:
                x += (" " + str("%.2f" % b)).rjust(4).ljust(7)
            else:
                x += str("%.2f" % b).rjust(4).ljust(7)
        x += "]\n"
    print(x)


def print_wolframalpha(A):
    x = "["
    for a in A:
        x += "["
        for b in a:
            x += str("%.0f" % b) + ", "
        x = x[:-2] + "],\n"
    x = x[:-2] + "]\n"
    print(x)


n = 3
m = 5

A = np.random.randint(0, 10, size=(n, m)).astype("float64")
B =row_reduce(copy.deepcopy(A))
print(sympy.Matrix(A).rref())
print(B)
