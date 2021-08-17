from collection import defaultdict


class ACTrie:

    def __init__(self):
        self.root = dict()


    def insert(self, word: str, order: int) -> None:
        if len(word) == 0:
            return

        sub_tree = self.root

        for c in word:
            if c not in sub_tree.keys():
                sub_tree[c] = dict()

            sub_tree = sub_tree[c]

        sub_tree['order'] = order


    def startswith(self, prefix: str) -> List[int]:
        result = []

        sub_tree = self.root
        for c in prefix:
            if c not in sub_tree.keys():
                return []
            sub_tree = sub_tree[c]

        result = self._traverse(sub_tree)

        return result


    def _traverse(self, root: dict) -> List[int]:
        result = []

        for branch in root.keys():
            if branch == 'order':
                result.append(root['order'])
            else:
                result.append(*self._traverse(root[branch]))

        return result


class bst_node:

    def __init__(self):
        self.left = None
        self.right = None
        self.val = None


class red_black_tree:

    def __init__(self):
        self.root = defaultdict(defaultdict)

    def left_rotate(self, sub_tree):
        x = sub_tree
        y = x['right']
        x['right'] = y['left']

        if y['left'] is not None:
            y['left']['parent'] = x



class AutocompleteSystem:
    '''
    https://leetcode.com/explore/learn/card/trie/148/practical-application-i/1054/

    句子自动补全

    如何更方便地对满足前缀的句子进行排序。这个是关键
    继续输入新的字符，也只是取原字库的子集。
    在输入新的字符后，如何更方便的剔除不满足的候选。要方便删除，那么候选结果肯定还得用一颗Trie存储。
    在正常情况下，键入新词后，筛掉了的候选往往要比留下的候选多得多。计算哪些被筛掉了不如遍历当前Trie的剩余的候选有效。

    input需要维持档期啊未结束的输入，保存缓存
    input接收到#的时候，需要走完全不同的逻辑路径
    '''

    def __init__(self, sentence: List[str], times: List[int]):
        self.trie = ACTrie()

        for i, w in enumerate(sentence):
            self.trie.insert(w, i)


    def input(self, c: str) -> List[str]:
        pass
