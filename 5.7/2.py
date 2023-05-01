class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 格式化字符串
        s = ''.join(filter(str.isalnum, s)).lower()
        # 双指针判断是否为回文串
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

作者：leejamesss
链接：https://leetcode.cn/problems/valid-palindrome/solution/yan-zheng-hui-wen-chuan-shuang-zhi-zhen-fan2t/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
