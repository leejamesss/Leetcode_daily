# https://leetcode.cn/problems/path-sum-ii/
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        res = []
        path = []
        self.dfs(root, targetSum, path, res)
        return res
    def dfs(self, root, target, path, res):
        if not root:
            return
        path.append(root.val)
        if not root.left and not root.right:
            if target == root.val:
                res.append(path[:])
        if root.left:
            self.dfs(root.left, target - root.val, path, res)
        if root.right:
            self.dfs(root.right, target - root.val, path, res)
        path.pop()
