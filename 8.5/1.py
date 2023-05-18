

class Solution:
    def bulbSwitch(self, n: int) -> int:
        cnt = [0] * (n + 1)
        for i in range(1, n + 1):
            j = i
            while j <= n:
                cnt[j] += 1
                j += i

        ans = 0
        for i in range(1, n + 1):
            if cnt[i] % 2 == 1:
                ans += 1

        return ans
#       https://leetcode.cn/problems/bulb-switcher/submissions/
