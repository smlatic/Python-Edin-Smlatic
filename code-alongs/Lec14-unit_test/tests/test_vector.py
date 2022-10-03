import sys, os
import unittest

print(__file__)

# we change directory to where the this file is
os.chdir(os.path.dirname(__file__))

# we jump back 1 step ../ , = define a path
# in this path we have vector.py and plotter.py and manual_testing.ipynb
path_to_vector_module = os.path.abspath("../")

sys.path.append(path_to_vector_module)
print(path_to_vector_module)

from vector import Vector

class TestVector(unittest.TestCase):
    def test_create_2d_vector(self):
        v = Vector(1, 2)
        self.assertEqual(v.numbers, (1, -2))
    
    def test_create_3d_vector(self):
        v = Vector(1, 2, 3)
        self.assertEqual(v.numbers, (1, 2, 3))



# 
if __name__ == "__main__":
    unittest.main()