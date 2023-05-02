# https://leetcode.cn/problems/word-ladder/submissions/
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        from collections import deque
    
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        preWords = {}
        for word in wordSet:
            for i in range(len(word)):
                key = word[:i] + "*" + word[i+1:]
                preWords[key] = preWords.get(key, []) + [word]

        # BFS搜索
        visited = set()
        queue = deque([(beginWord, 1)])
        while queue:
            curr_word, level = queue.popleft()
            for i in range(len(curr_word)):
                key = curr_word[:i] + "*" + curr_word[i+1:]
                for word in preWords.get(key, []):
                    if word == endWord:
                        return level + 1
                    if word not in visited:
                        visited.add(word)
                        queue.append((word, level+1))
                preWords[key] = []
        return 0
