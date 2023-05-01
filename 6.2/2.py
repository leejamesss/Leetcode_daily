# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(root,max_sum):
            if not root:
                return 0
            left_max = dfs(root.left,max_sum)
            right_max = dfs(root.right,max_sum)
            cur_max = root.val
            if left_max > 0:
                cur_max += left_max
            if right_max >0:
                cur_max += right_max
            max_sum[0] = max(max_sum[0], cur_max)
            return max(root.val,max(root.val+left_max,root.val+right_max))
        max_sum= [-1010]
        dfs(root,max_sum)
        return max_sum[0]
