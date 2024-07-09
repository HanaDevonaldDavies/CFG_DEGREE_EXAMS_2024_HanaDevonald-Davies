import unittest
from handshake import no_of_handshakes

class TestHandshake(unittest.TestCase):
    
    def test_handshakes(self):
    
        self.assertEqual(no_of_handshakes(2), 1)
        self.assertEqual(no_of_handshakes(1), 0)
    
    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            no_of_handshakes(-1)
        with self.assertRaises(ValueError):
            no_of_handshakes(0)
        with self.assertRaises(ValueError):
            no_of_handshakes("abc")
        

if __name__ == '__main__':
    unittest.main()