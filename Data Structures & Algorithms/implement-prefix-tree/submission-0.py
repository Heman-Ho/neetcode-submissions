class PrefixTree:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        cur_level = self.trie
        for c in word:
            if c in cur_level:
                cur_level = cur_level[c]
            else:
                cur_level[c] = {}
                cur_level = cur_level[c]
        cur_level['#'] = None

    def search(self, word: str) -> bool:
        cur_level = self.trie
        for c in word:
            if c not in cur_level:
                return False
            cur_level = cur_level[c]
        return '#' in cur_level

    def startsWith(self, prefix: str) -> bool:
        cur_level = self.trie
        for c in prefix:
            if c not in cur_level:
                return False
            cur_level = cur_level[c]
        return True
        
        