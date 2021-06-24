import unittest
from translator import engishtofrench, engishtogerman

class TestEnglishToFrench (unittest.TestCase):
    def test1(self):
        self.assertEqual(engishtofrench("Hello"), "Bonjour")
    def test2(self):
        self.assertIsNone(engishtofrench(None))
    def test3(self):
        self.assertEqual(engishtofrench("apple"), "Pomme")
        self.assertEqual(engishtofrench("my friend"), "Mon ami")

class TestEnglishToGerman (unittest.TestCase):
    def test1(self):
        self.assertEqual(engishtogerman("Hello"), "Hallo")
    def test2(self):
        self.assertIsNone(engishtogerman(None))
    def test3(self):
        self.assertEqual(engishtogerman("my friend"), "mein Freund")

if __name__ == '__main__':
    unittest.main()