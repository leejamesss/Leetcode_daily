class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        seen = set()
        last_occurrence = {c: i for i, c in enumerate(s)}
        
        for i, c in enumerate(s):
            if c not in seen:
                while stack and c < stack[-1] and last_occurrence[stack[-1]] > i:
                    seen.remove(stack.pop())
                seen.add(c)
                stack.append(c)
                
        return ''.join(stack)
#       https://leetcode.cn/problems/remove-duplicate-letters/submissions/
