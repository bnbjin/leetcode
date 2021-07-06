import math
import unittest


class TestTrees(unittest.TestCase()):
    def test_validate_binary_search_tree(self):
        '''
        https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/625/
        校验一颗树是否是二分搜索树BST

        中序遍历比较数值是否如预期
        '''

        def is_valid_bst(root):
            def inorder(root):
                if not root:
                    return True
                if not inorder(root.left):
                    return False
                if root.val <= self.prev:
                    return False
                self.prev = root.val
                return inorder(root.right)

            self.prev = -math.inf
            return inorder(root)
