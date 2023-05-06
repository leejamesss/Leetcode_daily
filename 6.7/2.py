# https://leetcode.cn/problems/candy/submissions/
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n # 初始化每个孩子的糖果数为 1

        # 从左往右遍历一次数组
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1

        # 从右往左遍历一次数组
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1] and candies[i] <= candies[i+1]:
                candies[i] = candies[i+1] + 1

        return sum(candies) # 返回总的糖果数
