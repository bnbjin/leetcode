class Trie:

    def __init__(self):
        self.root = dict()


    def insert(self, word: str) -> None:
        if len(word) == 0:
            return

        sub_tree = self.root

        for c in word:
            if c not in sub_tree.keys():
                sub_tree[c] = dict()

            sub_tree = sub_tree[c]

        sub_tree['word'] = True


    def search(self, word: str) -> bool:
        sub_tree = self.root
        for c in word:
            if c not in sub_tree.keys():
                return False
            sub_tree = sub_tree[c]

        return 'word' in sub_tree.keys() and sub_tree['word'] is True


    def startswith(self, prefix: str) -> bool:
        sub_tree = self.root
        for c in prefix:
            if c not in sub_tree.keys():
                return False
            sub_tree = sub_tree[c]

        return True
