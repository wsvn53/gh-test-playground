import unittest
from hello import hello

class TestHello(unittest.TestCase):
    def test_default(self):
        self.assertEqual(hello(), "Hello, World!")

    def test_custom_name(self):
        self.assertEqual(hello("Pikachu"), "Hello, Pikachu!")

if __name__ == "__main__":
    unittest.main()
