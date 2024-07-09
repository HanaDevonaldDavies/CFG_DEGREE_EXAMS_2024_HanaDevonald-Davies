import unittest
from handshake import no_of_handshakes

class TestHandshake(unittest.TestCase):
    
    def test_handshakes(self):
        # Test cases for valid inputs
        self.assertEqual(no_of_handshakes(2), 1)
        self.assertEqual(no_of_handshakes(3), 3)
        self.assertEqual(no_of_handshakes(20), 190)
        self.assertEqual(no_of_handshakes(1), 0)  # Edge case with one person
    
    def test_invalid_inputs(self):
        # Test cases for invalid inputs
        with self.assertRaises(ValueError):
            no_of_handshakes(-1)
        with self.assertRaises(ValueError):
            no_of_handshakes(0)
        with self.assertRaises(ValueError):
            no_of_handshakes("abc")
        with self.assertRaises(ValueError):
            no_of_handshakes(3.5)
        with self.assertRaises(ValueError):
            no_of_handshakes(None)

if __name__ == '__main__':
    unittest.main()