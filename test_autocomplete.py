from collection import defaultdict


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.data = None
        self.rank = 0


class ACTrie:
    '''
    https://leetcode.com/explore/learn/card/trie/148/practical-application-i/1054/

    句子自动补全

    如何更方便地对满足前缀的句子进行排序。这个是关键
    继续输入新的字符，也只是取原字库的子集。
    在输入新的字符后，如何更方便的剔除不满足的候选。要方便删除，那么候选结果肯定还得用一颗Trie存储。
    在正常情况下，键入新词后，筛掉了的候选往往要比留下的候选多得多。计算哪些被筛掉了不如遍历当前Trie的剩余的候选有效。

    input需要维持档期啊未结束的输入，保存缓存
    input接收到#的时候，需要走完全不同的逻辑路径

    PS: 当前实现并未如上述作相关优化实现，而是每次都DFS找
    PS: 当前实现未经测试
    '''

    def __init__(self, sentences, times):
        self.root = TrieNode()
        self.keyword = ""
        for i, sentence in enumerate(sentences):
            self.add_record(sentence, times[i])

    def add_record(self, sentence, times):
        node = self.root
        for char in sentence:
            if char not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end = True
        node.data = sentence
        node.rank += times

    def dfs(self, root):
        result = []
        if root:
            if root.is_end:
                result.append((root.rank, root.data))
            for child in root.children:
                result.extend(self.dfs(root.children[child]))
        return result

    def search(self, sentence):
        node = self.root
        for char in sentence:
            if char not in node.children:
                return []
            node = node.children[char]
        return self.dfs(node)

    def input(self, char):
        results = []
        if char != '#':
            self.keyword += c
            results = self.search(self.keyword)
        else:
            self.add_record(self.keyword, 1)
            self.keyword = ""
        return [item[1] for item in sorted(results, reverse=True)][:3]
