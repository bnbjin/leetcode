'''
https://leetcode.com/explore/learn/card/trie/149/practical-application-ii/1056/

Word Search II
'''

import unittest
from typing import List


class GraphNode:
    def __init__(self):
        self.left = None
        self.right = None
        self.top = None
        self.bottom = None
        self.value = None


class TrieNode:
    def __init__(self):
        self.children = {}


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.initializeTrie(board)

        inversed_result = set()
        for word in words:
            node = self.root
            for char in word:
                if char not in node.children:
                    inversed_result.add(word)
                    break
                node = node.children[char]

        words_set = set(words)
        result = words_set.difference(inversed_result)
        return list(result)

    def initializeTrie(self, board: List[List[str]]):
        self.root = TrieNode()

        for index_row, row in enumerate(board):
            for index_col, _ in enumerate(row):
                self.bfs_start(board, index_row, index_col, self.root)

    def bfs_start(self,
                  board: List[List[str]],
                  row: int,
                  col: int,
                  trieNode: TrieNode):
        self.grey_nodes = set()
        self.black_nodes = set()
        self.traverse_queue = []

        self.bfs(board, row, col, trieNode)

    # todo 更改为，无向有环图，
    # 无需置黑色节点，仅对于起始节点有效
    # 改变相关的判断条件
    def bfs(self,
            board: List[List[str]],
            row: int,
            col: int,
            trieNode: TrieNode):
        adjs = []
        if row > 0:
            adjs.append((row-1, col))
        if row < len(board)-1:
            adjs.append((row+1, col))
        if col > 0:
            adjs.append((row, col-1))
        if col < len(board[0])-1:
            adjs.append((row, col+1))

        for adj_vertex in adjs:
            arow, acol = adj_vertex[0], adj_vertex[1]
            self.grey_nodes.add(((arow, acol), (row, col)))
        self.traverse_queue.append((row, col))

        while len(self.traverse_queue) != 0:
            vertex = self.traverse_queue.pop()

            adjs = []
            if vertex[0] > 0:
                adjs.append((vertex[0]-1, vertex[1]))
            if vertex[0] < len(board)-1:
                adjs.append((vertex[0]+1, vertex[1]))
            if vertex[1] > 0:
                adjs.append((vertex[0], vertex[1]-1))
            if vertex[1] < len(board[0])-1:
                adjs.append((vertex[0], vertex[1]+1))

            for adj_vertex in adjs:
                arow, acol = adj_vertex[0], adj_vertex[1]
                if ((row, col), (arow, acol)) in self.grey_nodes \
                   or (arow, acol) in self.black_nodes:
                    continue

                ele = board[arow][acol]
                if ele not in trieNode.children:
                    trieNode.children[ele] = TrieNode()
                self.grey_nodes.add(((row, col), (arow, acol)))
                self.traverse_queue.append((arow, acol))
            self.black_nodes.add((row, col))


class TestWS2(unittest.TestCase):
    def test_normal(self):
        cases = [{
            'in': (
                [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
                ["oath","pea","eat","rain"]
            ),
            'out': ["eat","oath"]
        }, {
            'in': ([["a","b"],["c","d"]], ["abcb"]),
            'out': []
        }]

        for i, case in enumerate(cases):
            board = case['in'][0]
            words = case['in'][1]
            result = Solution().findWords(board, words)
            self.assertEqual(case['out'], result)
