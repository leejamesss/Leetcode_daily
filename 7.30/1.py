import heapq

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small = [] # 小根堆
        self.large = [] # 大根堆

    def addNum(self, num: int) -> None:
        # 添加元素到小根堆
        heapq.heappush(self.small, num)
        # 将小根堆的最小值移到大根堆中
        heapq.heappush(self.large, -heapq.heappop(self.small))
        # 保证两个堆的长度差不超过 1
        if len(self.small) < len(self.large):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        # 如果元素个数为偶数，则返回两堆堆顶元素的平均值
        if len(self.small) == len(self.large):
            return (self.small[0] - self.large[0]) / 2
        # 否则返回小根堆的堆顶元素
        else:
            return self.small[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
