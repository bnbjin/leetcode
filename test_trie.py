import unittest
from trie import Trie


class MapSum:
    '''
    https://leetcode.com/explore/learn/card/trie/148/practical-application-i/1058/
    '''

    def __init__(self):
        self.root = dict()

    def insert(self, key: str, val: int) -> None:
        st = self.root
        for c in key:
            if c not in st.keys():
                st[c] = dict()
            st = st[c]

        st['val'] = val

    def sum(self, prefix: str) -> int:
        st = self.root

        for c in prefix:
            if c not in st.keys():
                return 0
            st = st[c]

        return self.__traverse(st)

    def __traverse(self, root) -> int:
        sum = 0

        for branch in root.keys():
            if 'val' == branch:
                sum += root['val']
            else:
                sum += self.__traverse(root[branch])

        return sum


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

    def test_mapsum(self):
        ms = MapSum()

        ms.insert('apple', 3)
        self.assertEqual(3, ms.sum('ap'))

        ms.insert('app', 2)
        self.assertEqual(5, ms.sum('ap'))
