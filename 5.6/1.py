# https://leetcode.cn/problems/minimum-window-substring/
from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        # 统计 t 中每个字符的出现次数
        target = defaultdict(int)
        for c in t:
            target[c] += 1
        
        left, right = 0, 0
        count = 0  # 当前窗口中已经包含了多少个 t 中的字符
        ans_left, ans_right = -1, len(s) + 1  # 最小覆盖子串的起始位置和长度
        min_len = len(s) + 1
        
        while right < len(s):
            # 移动右指针扩大窗口
            if s[right] in target:
                if target[s[right]] > 0:
                    count += 1
                target[s[right]] -= 1
            
            right += 1
            
            # 移动左指针缩小窗口
            while count == len(t):
                if right - left < min_len:
                    ans_left, ans_right = left, right
                    min_len = right - left
                
                if s[left] in target:
                    target[s[left]] += 1
                    if target[s[left]] > 0:
                        count -= 1
                
                left += 1
        
        return s[ans_left:ans_right] if ans_left != -1 else ""
