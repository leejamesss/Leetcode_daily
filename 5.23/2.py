# https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def buildBST(left, right):
            if left > right:
                return None
            mid = left + (right - left) // 2
            root = TreeNode(nums[mid])
            root.left = buildBST(left, mid - 1)
            root.right = buildBST(mid + 1, right)
            return root

        return buildBST(0, len(nums) - 1)
