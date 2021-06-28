from quadroots import QuadRoots
import unittest

class TestQR(unittest.TestCase):


    def test_solve(self):
        qr = QuadRoots()
        qr.io()
        self.assertEqual(qr.io(),)
        print(qr.solve())
        pass



    def test_io(self):

        pass