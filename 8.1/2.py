class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * (4 * self.n)
        self.buildTree(nums, 0, 0, self.n - 1)

    def buildTree(self, nums, i, l, r):
        if l == r:
            self.tree[i] = nums[l]
            return
        mid = l + (r - l) // 2
        self.buildTree(nums, 2 * i + 1, l, mid)
        self.buildTree(nums, 2 * i + 2, mid + 1, r)
        self.tree[i] = self.tree[2 * i + 1] + self.tree[2 * i + 2]

    def update(self, i, val):
        self.updateHelper(i, val, 0, 0, self.n - 1)

    def updateHelper(self, i, val, index, l, r):
        if l == r:
            self.tree[index] = val
            return
        mid = l + (r - l) // 2
        if i <= mid:
            self.updateHelper(i, val, 2 * index + 1, l, mid)
        else:
            self.updateHelper(i, val, 2 * index + 2, mid + 1, r)
        self.tree[index] = self.tree[2 * index + 1] + self.tree[2 * index + 2]

    def sumRange(self, i, j):
        return self.sumRangeHelper(i, j, 0, 0, self.n - 1)

    def sumRangeHelper(self, i, j, index, l, r):
        if j < l or i > r:
            return 0
        if i <= l and j >= r:
            return self.tree[index]
        mid = l + (r - l) // 2
        left_sum = self.sumRangeHelper(i, j, 2 * index + 1, l, mid)
        right_sum = self.sumRangeHelper(i, j, 2 * index + 2, mid + 1, r)
        return left_sum + right_sum


class NumArray:
    def __init__(self, nums: List[int]):
        self.st = SegmentTree(nums)

    def update(self, index: int, val: int) -> None:
        self.st.update(index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.st.sumRange(left, right)
# https://leetcode.cn/problems/range-sum-query-mutable/submissions/
