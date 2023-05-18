
# https://leetcode.cn/problems/count-of-smaller-numbers-after-self/submissions/
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # 离散化
        sorted_nums = sorted(list(set(nums)))
        rank = {num: i+1 for i, num in enumerate(sorted_nums)}
        
        # 初始化树状数组
        n = len(nums)
        tree = [0] * (n+1)
        
        # 定义修改操作函数
        def update(i):
            while i <= n:
                tree[i] += 1
                i += lowbit(i)
         
        # 定义查询操作函数       
        def query(i):
            res = 0
            while i > 0:
                res += tree[i]
                i -= lowbit(i)
            return res
        
        # 倒序遍历数组
        ans = []
        for i in range(n-1, -1, -1):
            ans.append(query(rank[nums[i]]-1))  # 查询比 nums[i] 小的元素数量
            update(rank[nums[i]])  # 将 nums[i] 加入树状数组
        
        return ans[::-1]  # 最后按照原来的顺序返回答案

def lowbit(x):
    return x & (-x)
