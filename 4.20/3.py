# https://leetcode.cn/problems/insert-interval/
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        idx = 0

        # 将 newInterval 前面没有重叠的区间加入 res
        while idx < len(intervals) and intervals[idx][1] < newInterval[0]:
            res.append(intervals[idx])
            idx += 1

        # 合并所有和 newInterval 重叠的区间，更新 newInterval 的值
        while idx < len(intervals) and intervals[idx][0] <= newInterval[1]:
            newInterval = [min(newInterval[0], intervals[idx][0]), max(newInterval[1], intervals[idx][1])]
            idx += 1
        res.append(newInterval)

        # 将 newInterval 后面没有重叠的区间加入 res
        while idx < len(intervals):
            res.append(intervals[idx])
            idx += 1

        return res
