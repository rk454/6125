import math
import unittest

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
	size = A.__len__()
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

class TestStrassen(unittest.TestCase):
	def testStandardProduct(self):
		self.assertEqual(StandardProduct([[2]],[[3]]),[[6]])
		A = [[1,2,3],[4,5,6],[7,8,9]]
		B = [[3,2,1],[6,5,4],[9,8,7]]
		self.assertEqual(StandardProduct(A,B),[[42,36,30],[96,81,66],[150,126,102]])
		
	def testAdd(self):
		self.assertEqual(Add([[2]],[[3]]),[[5]])
		A = [[1,2,3],[4,5,6],[7,8,9]]
		B = [[3,2,1],[6,5,4],[9,8,7]]
		self.assertEqual(Add(A,B),[[4,4,4],[10,10,10],[16,16,16]])
		
	def testSubtract(self):
		self.assertEqual(Subtract([[2]],[[3]]),[[-1]])
		A = [[1,2,3],[4,5,6],[7,8,9]]
		B = [[3,2,1],[6,5,4],[9,8,7]]
		self.assertEqual(Subtract(A,B),[[-2,0,2],[-2,0,2],[-2,0,2]])
	
	def testStrassenProduct(self):
		self.assertEqual(StrassenProduct([[2]],[[3]],1),[[6]])
		A = [[1,2,3,4],[4,5,6,7],[7,8,9,10],[10,11,12,13]]
		B = [[4,3,2,1],[7,6,5,4],[10,9,8,7],[13,12,11,10]]
		self.assertEqual(StrassenProduct(A,B,1),[[100,90,80,70],[202,180,158,136],[304,270,236,202],[406,360,314,268]])
		
if __name__ == '__main__':
    unittest.main()