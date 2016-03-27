import unittest

def multiply(x, y):
    """ 
    multiplies two unsigned integer numbers in the Al Khwarizmi manner
    """
    if y == 0:
        return 0

    z = multiply(x, low_uint_bound_of_half(y))

    return 2 * z if is_even(y) else x + 2 * z



def low_uint_bound_of_half(number):
    """
    returns the low unsigned integer bound of a half of a number
    (it is simply a right shift method)
    """
    return number >> 1



def is_even(number):
    """
    tests whether the number is even
    """
    return number % 2 == 0



class AlgorithmTest(unittest.TestCase):

    def test_is_even_function(self):
        self.assertEqual(True, is_even(0))
        self.assertEqual(False, is_even(1))
        self.assertEqual(True, is_even(2))


    def test_low_uint_bound_of_half_function(self):
        self.assertEqual(0, low_uint_bound_of_half(0))
        self.assertEqual(0, low_uint_bound_of_half(1))
        self.assertEqual(1, low_uint_bound_of_half(2))
        self.assertEqual(1, low_uint_bound_of_half(3))

        self.assertEqual(0 >> 1, low_uint_bound_of_half(0))
        self.assertEqual(1 >> 1, low_uint_bound_of_half(1))
        self.assertEqual(2 >> 1, low_uint_bound_of_half(2))
        self.assertEqual(3 >> 1, low_uint_bound_of_half(3))


    def test_multiply_function(self):
        self.assertEqual(0, multiply(0, 10))
        self.assertEqual(10, multiply(1, 10))
        self.assertEqual(50, multiply(5, 10))



if __name__ == '__main__':
    unittest.main()
