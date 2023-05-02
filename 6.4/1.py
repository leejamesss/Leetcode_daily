
# https://leetcode.cn/problems/longest-consecutive-sequence/submissions/
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        for num in nums:
            if num-1 not in num_set: # 如果num是连续序列的开头
                curr_num = num
                curr_len = 1
                while curr_num+1 in num_set: # 向后查找最长连续序列
                    curr_num += 1
                    curr_len += 1
                longest = max(longest, curr_len) # 更新最长连续序列长度
        return longest
