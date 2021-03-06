import unittest
from Strassen import *
import math
import numpy as np

class TestStandardProduct(unittest.TestCase):
    def test_1d(self):
        self.assertEqual(StandardProduct([[2]],[[3]]),[[6]])

    def test_int(self):
        A = np.array([[1,2,3],[4,5,6],[7,8,9]])
        B = np.array([[3,2,1],[6,5,4],[9,8,7]])
        np.testing.assert_array_equal(StandardProduct(A,B),np.array([[42,36,30],[96,81,66],[150,126,102]]))

class TestAdd(unittest.TestCase):
    def test_1d(self):
        self.assertEqual(Add([[2]],[[3]]),[[5]])

    def test_int(self):
        A = np.array([[1,2,3],[4,5,6],[7,8,9]])
        B = np.array([[3,2,1],[6,5,4],[9,8,7]])
        np.testing.assert_array_equal(Add(A,B),np.array([[4,4,4],[10,10,10],[16,16,16]]))

class TestSubtract(unittest.TestCase):
    def test_1d(self):
        self.assertEqual(Subtract([[2]],[[3]]),[[-1]])

    def test_int(self):
        A = np.array([[1,2,3],[4,5,6],[7,8,9]])
        B = np.array([[3,2,1],[6,5,4],[9,8,7]])
        np.testing.assert_array_equal(Subtract(A,B),np.array([[-2,0,2],[-2,0,2],[-2,0,2]]))
        

class TestFast_Add(unittest.TestCase):
    def test_1d(self):
        self.assertEqual(Fast_Add([[2]],[[3]],2),[[5]])

    def test_int(self):
        A = np.array([[1,2,3],[4,5,6],[7,8,9]])
        B = np.array([[3,2,1],[6,5,4],[9,8,7]])
        np.testing.assert_array_equal(Fast_Add(A,B,2),np.array([[4,4,4],[10,10,10],[16,16,16]]))

class TestFast_Subtract(unittest.TestCase):
    def test_1d(self):
        self.assertEqual(Fast_Subtract([[2]],[[3]],2),[[-1]])

    def test_int(self):
        A = np.array([[1,2,3],[4,5,6],[7,8,9]])
        B = np.array([[3,2,1],[6,5,4],[9,8,7]])
        np.testing.assert_array_equal(Fast_Subtract(A,B,2),np.array([[-2,0,2],[-2,0,2],[-2,0,2]]))

class TestStrassenProduct(unittest.TestCase):
    def test_id(self):
        self.assertEqual(StrassenProduct([[2]],[[3]],1),[[6]])

    def test_int(self):
        A = np.array([[1,2,3,4],[4,5,6,7],[7,8,9,10],[10,11,12,13]])
        B = np.array([[4,3,2,1],[7,6,5,4],[10,9,8,7],[13,12,11,10]])
        np.testing.assert_array_equal(StrassenProduct(A,B,1),np.array([[100,90,80,70],[202,180,158,136],[304,270,236,202],[406,360,314,268]]))
        
    def test_rand_float(self):
        np.random.seed(1)
        A = np.random.rand(4,4)
        print A
        B = np.random.rand(4,4)
        print "numpy", StandardProduct(A,B)
        print "strassen", StrassenProduct(A,B,1)

class TestProduct(unittest.TestCase):        
    def test_notpow2(self):
        A = np.array([[1,2,3],[4,5,6],[7,8,9]])
        B = np.array([[3,2,1],[6,5,4],[9,8,7]])
        np.testing.assert_array_equal(Product(A,B,1),np.array([[42,36,30],[96,81,66],[150,126,102]]))

if __name__ == '__main__':
    unittest.main()