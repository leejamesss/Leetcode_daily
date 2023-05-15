class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_word = False

class WordDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if not node.children[idx]:
                node.children[idx] = TrieNode()
            node = node.children[idx]
        node.is_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self._search_word(self.root, word)

    def _search_word(self, node: TrieNode, word: str) -> bool:
        if not node:
            return False
        if not word:
            return node.is_word
        if word[0] == '.':
            for child in node.children:
                if self._search_word(child, word[1:]):
                    return True
        else:
            idx = ord(word[0]) - ord('a')
            return self._search_word(node.children[idx], word[1:])
        return False

#  https://leetcode.cn/problems/design-add-and-search-words-data-structure/
