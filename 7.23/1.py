class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        res = []
        for num, count in counts.items():
            if count == 1:
                res.append(num)
        
        return res
# https://leetcode.cn/problems/single-number-iii/submissions/
