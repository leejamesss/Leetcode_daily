class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def dfs(node, path):
            if not node.left and not node.right:
                res.append(path)
                return
            if node.left:
                dfs(node.left, path + "->" + str(node.left.val))
            if node.right:
                dfs(node.right, path + "->" + str(node.right.val))
        
        res = []
        if not root:
            return res
        dfs(root, str(root.val))
        return res
# https://leetcode.cn/problems/binary-tree-paths/submissions/
