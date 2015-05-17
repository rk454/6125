import math
import numpy as np

def StandardProduct(A,B): # A and B are squared matrices of the same size
    size = A.__len__()
    C = [[0 for x in range(size)] for x in range(size)]
    for i in range(size):
        for j in range(size):
            for k in range(size):
                C[i][j] += A[i][k]*B[k][j]
    return C

def Add(A,B): # returns A+B
    size = A.__len__()
    C = [[0 for x in range(size)] for x in range(size)]
    for i in range(size):
            for j in range(size):
                C[i][j] = A[i][j] + B[i][j]
    return C

def Subtract(A,B): # returns A-B
    size = A.__len__()
    C = [[0 for x in range(size)] for x in range(size)]
    for i in range(size):
        for j in range(size):
            C[i][j] = A[i][j] - B[i][j]
    return C

def StrassenProduct(A,B,threshold): # assuming the size of A and B are minimal size * 2^n where minimal size < threshold
    size = len(A)
    sizeB = len(B)
    # check if matrices meet the requirements of Strassen
    if size != len(A[0]) or (size & (size-1)) != 0:
        print "Error: The first matrix is not square or its size is not 2^n!"
        return None
    elif sizeB != len(B[0]) or (sizeB & (sizeB - 1)) != 0:
        print "Error: The second matrix is not square or its size is not 2^n!"
        return None

    # perform standard product if the size is smaller than threshold
    if size <= threshold:
        C = StandardProduct(A,B)
    else:
        # partition
        halfsize = int(size/2)
        A11 = [[0 for x in range(halfsize)] for x in range(halfsize)]
        A12 = [[0 for x in range(halfsize)] for x in range(halfsize)]
        A21 = [[0 for x in range(halfsize)] for x in range(halfsize)]
        A22 = [[0 for x in range(halfsize)] for x in range(halfsize)]

        B11 = [[0 for x in range(halfsize)] for x in range(halfsize)]
        B12 = [[0 for x in range(halfsize)] for x in range(halfsize)]
        B21 = [[0 for x in range(halfsize)] for x in range(halfsize)]
        B22 = [[0 for x in range(halfsize)] for x in range(halfsize)]

        for i in range(halfsize):
            for j in range(halfsize):
                A11[i][j] = A[i][j]
                A12[i][j] = A[i][j+halfsize]
                A21[i][j] = A[i+halfsize][j]
                A22[i][j] = A[i+halfsize][j+halfsize]
                B11[i][j] = B[i][j]
                B12[i][j] = B[i][j+halfsize]
                B21[i][j] = B[i+halfsize][j]
                B22[i][j] = B[i+halfsize][j+halfsize]

        # compute intermediate matrices
        M1 = StrassenProduct(Add(A11,A22),Add(B11,B22),threshold)
        M2 = StrassenProduct(Add(A21,A22),B11,threshold)
        M3 = StrassenProduct(A11,Subtract(B12,B22),threshold)
        M4 = StrassenProduct(A22,Subtract(B21,B11),threshold)
        M5 = StrassenProduct(Add(A11,A12),B22,threshold)
        M6 = StrassenProduct(Subtract(A21,A11),Add(B11,B12),threshold)
        M7 = StrassenProduct(Subtract(A12,A22),Add(B21,B22),threshold)

        C = [[0 for x in range(size)] for x in range(size)]
        for i in range(halfsize):
            for j in range(halfsize):
                C[i][j] = M1[i][j] + M4[i][j] - M5[i][j] + M7[i][j]
                C[i][j+halfsize] = M3[i][j] + M5[i][j]
                C[i+halfsize][j] = M2[i][j] + M4[i][j]
                C[i+halfsize][j+halfsize] = M1[i][j] - M2[i][j] + M3[i][j] + M6[i][j]

    return C

if __name__ == "__main__":
    np.random.seed(1)
    A = np.random.rand(6,6)
    B = np.random.rand(6,6)
    StrassenProduct(A,B,1)
    pass
