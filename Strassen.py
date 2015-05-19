import math
import numpy as np

def StandardProduct(A,B): # A and B are squared matrices of the same size
    size = A.__len__()
    C = [[0 for x in xrange(size)] for x in xrange(size)]
    for i in xrange(size):
        for j in xrange(size):
            for k in xrange(size):
                C[i][j] += A[i][k]*B[k][j]
    return C

def Add(A,B): # returns A+B
    size = A.__len__()
    C = [[A[i][j] + B[i][j] for j in xrange(size)] for i in xrange(size)]
    return C

def Subtract(A,B): # returns A-B
    size = A.__len__()
    C = [[A[i][j] - B[i][j] for j in xrange(size)] for i in xrange(size)]
    return C


def Fast_Add(A,B,b_size): # returns A+B
    size = A.__len__()
    C = [[0 for x in range(size)] for x in range(size)]
    for i in xrange(0,size,b_size):
            for j in xrange(0,size,b_size):
                for k in xrange(i,min(size,i+b_size)):
                    for l in xrange(j,min(size,j+b_size)):
                        C[k][l] = A[k][l] + B[k][l]
    return C

def Fast_Subtract(A,B,b_size): # returns A-B
    size = A.__len__()
    C = [[0 for x in range(size)] for x in range(size)]
    for i in xrange(0,size,b_size):
            for j in range(0,size,b_size):
                for k in xrange(i,min(size,i+b_size)):
                    for l in xrange(j,min(size,j+b_size)):
                        C[k][l] = A[k][l] - B[k][l]

    return C


def StrassenProduct(A,B,threshold): # assuming the size of A and B are minimal size * 2^n where minimal size < threshold
    size = len(A)
    # perform standard product if the size is smaller than threshold
    if size <= threshold:
        C = StandardProduct(A,B)
    else:
        # partition
        halfsize = int(size/2)
        A11 = [x[:halfsize] for x in A[:halfsize]]
        A12 = [x[halfsize:] for x in A[:halfsize]]
        A21 = [x[:halfsize] for x in A[halfsize:]]
        A22 = [x[halfsize:] for x in A[halfsize:]]

        B11 = [x[:halfsize] for x in B[:halfsize]]
        B12 = [x[halfsize:] for x in B[:halfsize]]
        B21 = [x[:halfsize] for x in B[halfsize:]]
        B22 = [x[halfsize:] for x in B[halfsize:]]


        # compute intermediate matrices
        M1 = StrassenProduct(Add(A11,A22),Add(B11,B22),threshold)
        M2 = StrassenProduct(Add(A21,A22),B11,threshold)
        M3 = StrassenProduct(A11,Subtract(B12,B22),threshold)
        M4 = StrassenProduct(A22,Subtract(B21,B11),threshold)
        M5 = StrassenProduct(Add(A11,A12),B22,threshold)
        M6 = StrassenProduct(Subtract(A21,A11),Add(B11,B12),threshold)
        M7 = StrassenProduct(Subtract(A12,A22),Add(B21,B22),threshold)

        C = [[0 for x in xrange(size)] for x in xrange(size)]
        for i in xrange(halfsize):
            for j in xrange(halfsize):
                C[i][j] = M1[i][j] + M4[i][j] - M5[i][j] + M7[i][j]
                C[i][j+halfsize] = M3[i][j] + M5[i][j]
                C[i+halfsize][j] = M2[i][j] + M4[i][j]
                C[i+halfsize][j+halfsize] = M1[i][j] - M2[i][j] + M3[i][j] + M6[i][j]

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
        A1 = [[0 for x in xrange(size)] for x in xrange(size)]
        B1 = [[0 for x in xrange(size)] for x in xrange(size)]
        for i in xrange(sizeA):
            for j in xrange(sizeA):
                A1[i][j] = A[i][j]
        for i in xrange(sizeB):
            for j in xrange(sizeB):
                B1[i][j] = B[i][j]
        C = StrassenProduct(A1,B1,threshold)
        return [[C[i][j] for j in xrange(sizeA)] for i in range(sizeA)]


if __name__ == "__main__":
    import time
    import matplotlib.pyplot as plt

    np.random.seed(2)
    strassenTime = []
    standardTime = []

    for i in xrange(31):
        n = 2**i
        A = np.random.rand(n,n)
        B = np.random.rand(n,n)

        s1 = time.time()
        strassen = StrassenProduct(A,B,1)
        e1 = time.time()
        strassenTime.append(np.log2(e1-s1))

        s2 = time.time()
        standard = StandardProduct(A,B)
        e2 = time.time()
        standardTime.append(np.log2(e2-s2))

    # plt.clf()
    plt.figure()
    plt.plot(strassenTime, color='b', label = 'strassen')
    plt.plot(standardTime, color='r', label = 'standard')
    plt.legend()
    plt.title("Performance comparison of Strassen Product vs. Standard Product")
    plt.xlabel("Log (base 2) size of the matrices multiplied")
    plt.ylabel("Log (base 2) Time")
    plt.show()

