# https://leetcode.cn/problems/largest-number/
class LargerNumKey(str):
    def __lt__(x, y):
        return x + y > y + x

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # 将整数列表转化为字符串列表
        nums = [str(num) for num in nums]
        # 对字符串列表进行自定义比较函数排序
        nums.sort(key=LargerNumKey)
        # 如果最大的数是 0，则直接返回 "0"，否则将所有字符串拼接起来得到结果
        return '0' if nums[0] == '0' else ''.join(nums)
