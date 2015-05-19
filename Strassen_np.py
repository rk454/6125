import math
import numpy as np

def StandardProduct(A,B): # A and B are squared matrices of the same size
    size = len(A)
    C = np.empty([size,size])
    for i in xrange(size):
        for j in xrange(size):
            C[i,j] = sum([A[i,k]*B[k,j] for k in xrange(size)])
    return C

def Add(A,B): # returns A+B
    size = len(A)
    C = [[A[i][j] + B[i][j] for j in xrange(size)] for i in xrange(size)]
    return C

def Subtract(A,B): # returns A-B
    size = len(A)
    C = [[A[i][j] - B[i][j] for j in xrange(size)] for i in xrange(size)]
    return C


def Fast_Add(A,B,b_size): # returns A+B
    size = A.__len__()
    C = [[0 for x in range(size)] for x in range(size)]
    for i in xrange(0,size,b_size):
            for j in xrange(0,size,b_size):
                C[i:b_size,j:b_size] = A[i:b_size,j:b_size] + B[i:b_size,j:b_size]
    return C

def Fast_Subtract(A,B,b_size): # returns A-B
    size = A.__len__()
    C = np.empty([size,size])
    for i in xrange(0,size,b_size):
            for j in range(0,size,b_size):
                C[i:b_size,j:b_size] = A[i:b_size,j:b_size] - B[i:b_size,j:b_size]
    return C


def StrassenProduct(A,B,threshold): # assuming the size of A and B are minimal size * 2^n where minimal size < threshold
    size = len(A)
    # perform standard product if the size is smaller than threshold
    if size <= threshold:
        C = StandardProduct(A,B)
    else:
        # partition
        halfsize = int(size/2)
        A11 = A[:halfsize,:halfsize]
        A12 = A[:halfsize,halfsize:]
        A21 = A[halfsize:,:halfsize]
        A22 = A[halfsize:,halfsize:]

        B11 = B[:halfsize,:halfsize]
        B12 = B[:halfsize,halfsize:]
        B21 = B[halfsize:,:halfsize]
        B22 = B[halfsize:,halfsize:]


        # compute intermediate matrices
        M1 = StrassenProduct(A11+A22,B11+B22,threshold)
        M2 = StrassenProduct(A21+A22,B11,threshold)
        M3 = StrassenProduct(A11,B12-B22,threshold)
        M4 = StrassenProduct(A22,B21-B11,threshold)
        M5 = StrassenProduct(A11+A12,B22,threshold)
        M6 = StrassenProduct(A21-A11,B11+B12,threshold)
        M7 = StrassenProduct(A12-A22,B21+B22,threshold)
        C = np.empty([size,size])
        C[:halfsize,:halfsize] = M1[:halfsize,:halfsize] + M4[:halfsize,:halfsize] - M5[:halfsize,:halfsize] + M7[:halfsize,:halfsize]
        C[:halfsize,halfsize:] = M3[:halfsize,:halfsize] + M5[:halfsize,:halfsize]
        C[halfsize:,:halfsize] = M2[:halfsize,:halfsize] + M4[:halfsize,:halfsize]
        C[halfsize:,halfsize:] = M1[:halfsize,:halfsize] - M2[:halfsize,:halfsize] + M3[:halfsize,:halfsize] + M6[:halfsize,:halfsize]
    return C

def Product(A,B,threshold):
    sizeA = len(A)
    sizeB = len(B)
    # check if matrices meet the requirements of Strassen
    if sizeA != len(A[0]):
        print "Error: The first matrix is not square!"
        return None
    elif sizeB != len(B[0]):
        print "Error: The second matrix is not square!"
        return None
    elif len(A[0]) != sizeB:
        print "Matrix dimension mismatch!"
        return None

    if (sizeA & sizeA-1) == 0: # Matrix dimension is 2^n x 2^n
        return StrassenProduct(A,B,threshold)

    else: # Matrix dimension is not 2^N, create 2^N matrix by padding zeros
        size = 2**sizeA.bit_length()
        A1 = np.zeros([size,size])
        B1 = np.zeros([size,size])
        A1[:sizeA,:sizeB] = A
        B1[:sizeB,:sizeB] = B
        C = StrassenProduct(A1,B1,threshold)
        return C[:sizeA,:sizeA]


if __name__ == "__main__":
    pass
