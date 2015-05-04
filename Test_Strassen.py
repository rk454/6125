import unittest
import Strassen
import math

class TestStrassen(unittest.TestCase):
	def TestStandardProduct(self):
		self.assertEqual(StandardProduct([2],[3]),[6])
		A = [[1,2,3],[4,5,6],[7,8,9]]
		B = [[3,2,1],[6,5,4],[9,8,7]]
		self.assertEqual(StandardProduct(A,B),[[42,36,30],[96,81,66],[150,126,102]])
		
	def TestAdd(self):
		self.assertEqual(Add([2],[3]),[5])
		A = [[1,2,3],[4,5,6],[7,8,9]]
		B = [[3,2,1],[6,5,4],[9,8,7]]
		self.assertEqual(Add(A,B),[[4,4,4],[10,10,10],[16,16,16]])
		
	def TestSubtract(self):
		self.assertEqual(Subtract([2],[3]),[-1])
		A = [[1,2,3],[4,5,6],[7,8,9]]
		B = [[3,2,1],[6,5,4],[9,8,7]]
		self.assertEqual(Subtract(A,B),[[-2,0,2],[-2,0,2],[-2,0,2]])
	
	def TestStrassenProduct(self):
		self.assertEqual(StrassenProduct([2],[3],1),[6])
		A = [[1,2,3,4],[4,5,6,7],[7,8,9,10],[10,11,12,13]]
		B = [[4,3,2,1],[7,6,5,4],[10,9,8,7],[13,12,11,10]]
		self.assertEqual(StrassenProduct(A,B,1),[[100,90,80,70],[202,180,158,136],[304,270,236,202],[406,360,314,268]])