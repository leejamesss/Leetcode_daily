# https://leetcode.cn/problems/permutations-ii/
#回溯
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        nums.sort()  # 先将数组排序，方便后面去重
        
        def backtrack(first):
            nonlocal ans
            
            if first == n:
                ans.append(nums[:])
            
            used = set()  # 用来记录当前位置已经填过哪些数字
            for i in range(first, n):
                # 如果当前位置与前面的数字相等，并且前面的数字还没填过，直接跳过
                if nums[i] in used:
                    continue
                
                used.add(nums[i])
                nums[first], nums[i] = nums[i], nums[first]  # 交换数字
                backtrack(first+1)  # 处理下一个位置
                nums[first], nums[i] = nums[i], nums[first]  # 回溯操作
              
        backtrack(0)
        return ans
