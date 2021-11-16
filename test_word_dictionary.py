'''
https://leetcode.com/explore/learn/card/trie/148/practical-application-i/1052/
'''

import unittest


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word.lower():
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def searchSub(self, node: TrieNode, word: str) -> bool:
        for i, char in enumerate(word):
            if char == '.':
                for child in node.children:
                    if self.searchSub(node.children[child], word[i+1:]):
                        return True
                return False
            else:
                if char in node.children:
                    node = node.children[char]
                else:
                    return False
        return node.is_end

    def search(self, word: str) -> bool:
        return self.searchSub(self.root, word.lower())


class TestWD(unittest.TestCase):
    def test_normal(self):
        wd = WordDictionary()
        wd.addWord("bad")
        wd.addWord("dad")
        wd.addWord("mad")
        self.assertFalse(wd.search("pad"))
        self.assertTrue(wd.search("bad"))
        self.assertTrue(wd.search(".ad"))
        self.assertTrue(wd.search("b.."))
