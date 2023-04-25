# https://leetcode.cn/problems/unique-binary-search-trees-ii/submissions
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        
        def generate(start, end):
            if start > end:
                return [None]
            res = []
            for i in range(start, end+1):
                left_trees = generate(start, i-1)
                right_trees = generate(i+1, end)
                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        res.append(root)
            return res
        
        return generate(1, n)
