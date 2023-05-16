from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n == 0:
            return []
        # 初始队列：存储前k个元素中最大值的索引
        deque_index = deque([0])
        # 初始化结果数组
        res = [max(nums[:k])]
        for i in range(1, n):
            # 如果队头元素超出了滑动窗口的范围，弹出队头元素
            if deque_index[0] < i-k+1:
                deque_index.popleft()
            # 如果队列中有比 nums[i] 小的元素，弹出它们
            while deque_index and nums[deque_index[-1]] < nums[i]:
                deque_index.pop()
            # 将 nums[i] 加入队列尾部
            deque_index.append(i)
            # 如果当前索引 i 大于等于 k-1，说明已经形成了一个完整的大小为 k 的滑动窗口
            if i >= k-1:
                res.append(nums[deque_index[0]])
        return res
# https://leetcode.cn/problems/sliding-window-maximum/
