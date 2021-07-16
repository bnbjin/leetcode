import unittest
from trie import Trie


class TestTrie(unittest.TestCase):

    def test_normal(self):
        t = Trie()
        t.insert('wordtest')
        self.assertTrue(t.search('wordtest'))
        self.assertFalse(t.search('wordtest2'))
        self.assertFalse(t.search('wordtes'))
        self.assertTrue(t.startswith('word'))
        self.assertTrue(t.startswith('wordtest'))
        self.assertFalse(t.startswith('wordtest1'))
        self.assertFalse(t.startswith('wordtess'))
