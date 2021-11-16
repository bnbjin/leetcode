import unittest
from trie import Trie

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.data = None
        self.rank = 0

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

    def test_replace_words(self):
        '''
        https://leetcode.com/explore/learn/card/trie/148/practical-application-i/1053/
        '''

        def replace_words(dictionary, sentence):
            t = Trie()
            for w in dictionary:
                t.insert(w)

            result = ""
            for w in sentence.split():
                pre = t.get_prefix(w)
                if pre != "":
                    result += pre
                else:
                    result += w
                result += " "

            result = result.rstrip()

            return result

        cases = [
            {
                'dic': ['catt', 'cat', 'bat', 'rat'],
                'sentence': "the cattle was rattled by the battery",
                'output': "the cat was rat by the bat",
            }, {
                'dic': ['ac', 'ab'],
                'sentence': "it is abnormal that this solution is accepted",
                'output': "it is ab that this solution is ac",
            }
        ]

        for c in cases:
            self.assertEqual(c['output'],
                             replace_words(c['dic'], c['sentence']))
