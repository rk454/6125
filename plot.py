import time
import matplotlib.pyplot as plt
import numpy as np
import Strassen
import Strassen_np

def ComparisonPlot(method, maxSize):
    np.random.seed(1)
    strassenTime = []
    standardTime = []

    for i in xrange(maxSize):
        n = 2**i
        A = np.random.rand(n,n)
        B = np.random.rand(n,n)

        s1 = time.time()
        strassen = method.StrassenProduct(A,B,1)
        e1 = time.time()
        strassenTime.append(np.log2(e1-s1))

        s2 = time.time()
        standard = method.StandardProduct(A,B)
        e2 = time.time()
        standardTime.append(np.log2(e2-s2))

        print "completed size 2^", i
    # plt.clf()
    plt.figure()
    plt.plot(strassenTime, color='b', label = 'strassen')
    plt.plot(standardTime, color='r', label = 'standard')
    plt.legend()
    plt.title("Performance comparison of Strassen Product vs. Standard Product")
    plt.xlabel("Log (base 2) size of the matrices multiplied")
    plt.ylabel("Log (base 2) Time")
    plt.show()


if __name__ == "__main__":
    ComparisonPlot(Strassen_np, 11)