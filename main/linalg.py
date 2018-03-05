import numpy as np
import random
import time
from matplotlib import pyplot as plt
def row_reduce(A):

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


def det(A):
    if np.shape(A) == (1, 1):
        return A
    else:
        D = 0
        for i, k in enumerate(A[0]):
            D += k * det(np.concatenate(((A[1:][..., 0:i]).T, (A[1:][..., i+1:]).T)).T) * (-1)**i
        return D


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


def generate_random_matrix(m, n, element_range):
    return np.array([[random.randint(0, element_range) for j in range(n)] for i in range(m)], dtype="float64")


B = [
    [[12,7,11,-9,5],
     [-9,4,-27,9,-3],
     [-6,11,-7,3,-4],
     [4,-6,10,-5,12]],
    [[4,-6,10,-5,12],
     [4,-6,10,-5,12],
     [4,-6,10,-5,12],
     [4,-6,10,-5,12]],
    [[10, 2, 3, 4],
     [20, 2, 3, 4],
     [30, 2, 3, 4],
     [40, 2, 3, 4]],
    [[10, 2, 3, 4, 5],
     [20, 2, 3, 4, 5],
     [30, 2, 3, 4, 5],
     [40, 2, 3, 4, 5]],
    [[4, -6, 10, -5, 12, 12, 7, 11, -9, 5],
     [-9, 4, -27, 9, -3, 42, 7, 13, -9, 5],
     [4, -4, 10, -5, 14, 12, 7, 11, -9, 5],
     [4, -6, 10, -5, 12, -6, 11, -7, 3, -4],
     [12, 7, 11, -9, 5, -6, 11, -7, 3, -4],
     [-9, 4, -27, 9, -3, -9, 4, -27, 9, -3],
     [-6, 11, -7, 3, -4, -9, 4, -27, 9, -3],
     [4, -6, 10, -5, 12, 10, -5, 12, -6, 11]],
    [[4, -6, 10, -5, 12, 12, 7, 11, -9, 5, 4, -6, 10, -5, 12, -6, 11, -7, 3, -4],
     [-9, 4, -27, 9, -3, 42,9, -3, -9, 4, -27, 9, -3, 4, -6, 10, 7, 13, -9, 5],
     [4, -4, 10, -5, 14, 12, 7, 11, -9, 5, 4, -6, 10, -5, 12, -6, 11, -7, 3, -4],
     [4, -6, 10, -5, 12, -6, 11, -7, 3, -4, 9, -3, -9, 4, -27, 9, -3, 4, -6, 10],
     [12, 7, 11, 9, -3, -9, 4, -27, 9, -3, 4, -6, 10, -9, 5, -6, 11, -7, 3, -4],
     [-9, 4, -27, 9, -3, -9, 4, -27, 9, -3, 4, -6, 10, -5, 12, -6, 11, -7, 3, -4],
     [-6, 11, -7, 3, -4, -9, 4, -27, 9, -3, 12, 7, 11,9, -3, -9, 4, -27, 9, -3],
     [4, -6, 10, -5, 12, -9, 4, -27, 9, -3, -3, -9, 4, -27, 9, -3, -5, 12, -6, 11],
     [4, -6, 10, -5, 12, -6, 11, -7, 3, -4, 9, -3, -9, 4, -27, 9, -3, 4, -6, 10],
     [12, 7, 11, 9, -3, -9, 4, -27, 9, -9, 4, -27, 9, -3, 4, -6, 11, -7, 3, -4]],
    [[4, -6, 10, -5, 12, 12, 7, 11, -9, 5],
     [-9, 4, -27, 9, -3, 42, 7, 13, -9, 5],
     [4, -4, 10, -5, 14, 12, 7, 11, -9, 5],
     [4, -6, 10, -5, 12, -6, 11, -7, 3, -4]],
     [[4, -6, 10, -5, 12, 12, 7, 11, -9, 5, 4, -6, 10, -5, 12, -6, 11, -7, 3, -4],
      [-9, 4, -27, 9, -3, 42, 9, -3, -9, 4, -27, 9, -3, 4, -6, 10, 7, 13, -9, 5],
      [4, -4, 10, -5, 14, 12, 7, 11, -9, 5, 4, -6, 10, -5, 12, -6, 11, -7, 3, -4],
      [4, -6, 10, -5, 12, -6, 11, -7, 3, -4, 9, -3, -9, 4, -27, 9, -3, 4, -6, 10],
      [4, -6, 10, -5, 12, -6, 11, -7, 3, -4, 9, -3, -9, 4, -27, 9, -3, 4, -6, 10],
      [12, 7, 11, 9, -3, -9, 4, -27, 9, -3, 4, -6, 10, -9, 5, -6, 11, -7, 3, -4],
      [-9, 4, -27, 9, -3, -9, 4, -27, 9, -3, 4, -6, 10, -5, 12, -6, 11, -7, 3, -4],
      [-6, 11, -7, 3, -4, -9, 4, -27, 9, -3, 12, 7, 11, 9, -3, -9, 4, -27, 9, -3, ],
      [4, -6, 10, -5, 12, -9, 4, -27, 9, -3, -3, -9, 4, -27, 9, -3, -5, 12, -6, 11],
      [12, 7, 11, 9, -3, -9, 4, -27, 9, -9, 4, -27, 9, -3, 4, -6, 11, -7, 3, -4]]
     ]


WSW7 = [[1, 0, 3, 0, 0, 0],
        [1, 8, 5, 2, 0, 0],
        [1, 6, 6, 0, 1, 0],
        [3, 7, 7, 1, 2, 0]]
ns = np.arange(1, 1000, 1)
#fil = open("fil.txt", "w")
#for n in ns:
#    t = time.clock()
#    A = generate_random_matrix(n, n, 10)
#    sd = row_reduce(A)
#    t = time.clock() - t
#    fil.write(str(n) + "\t" + str(t) + "\n")
#    if n % 10 == 0:
#        fil.close()
#        fil = open("fil.txt", "a")

#fil.close()


print(det(np.array([[3, 7], [5, 9]])))