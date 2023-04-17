
# https://leetcode.cn/problems/letter-combinations-of-a-phone-number/
#回溯法
#字典，每个数字映射到它可能表示的字符集合中
#从字符串的第一个数字开始，递归地构建所有可能的组合
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digit_map = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        n = len(digits)
        ans = []
        
        def backtrack(index, cur_str):
            if index == n:
                ans.append(cur_str)
                return
            for c in digit_map[digits[index]]:
                backtrack(index+1, cur_str+c)
                
        backtrack(0, '')
        return ans
