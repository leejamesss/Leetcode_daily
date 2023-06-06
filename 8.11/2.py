class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # 初始化两个最小值
        min1 = float('inf')
        min2 = float('inf')
        
        for num in nums:
            if num <= min1:
                # 如果当前数比第一个最小值还小，就更新第一个最小值
                min1 = num
            elif num <= min2:
                # 如果当前数比第一个最小值大但比第二个最小值小，就更新第二个最小值
                min2 = num
            else:
                # 如果当前数比第二个最小值还大，说明已经找到了递增的三元组
                return True
        
        # 没有找到递增的三元组
        return False
# https://leetcode.cn/problems/increasing-triplet-subsequence/submissions/
