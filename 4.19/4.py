#https://leetcode.cn/problems/merge-intervals/submissions/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals.sort(key=lambda x: x[0])  # 按照左端点从小到大排序
        merged = []
        for i in range(n):
            if not merged or merged[-1][1] < intervals[i][0]:  # 如果当前区间无法和前一个区间合并，则直接加入答案
                merged.append(intervals[i])
            else:  # 否则，合并当前区间和前一个区间
                merged[-1][1] = max(merged[-1][1], intervals[i][1])
        return merged
