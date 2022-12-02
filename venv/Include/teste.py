import unittest
import root_square_solver import rootSquareSolver 

class CheckRootSquareSolver(unittest.TestCase):

    def test_checkTwoRoots(self):
        response = rootSquareSolver(1,-5,6)
        self.assertEqual(len(response),2)

    def test_checkRootValue1(self):
        response = rootSquareSolver(1,-5,6)
        self.assertIn(response[0],[2,3])

    def test_checkRootValue2(self):
        response = rootSquareSolver(1,-5,6)
        self.assertIn(response[1],[2,3])