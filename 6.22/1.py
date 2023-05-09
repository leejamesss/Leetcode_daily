# https://leetcode.cn/problems/binary-search-tree-iterator/submissions/
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self.cur = root

    def hasNext(self) -> bool:
        return self.cur is not None or len(self.stack) > 0

    def next(self) -> int:
        while self.cur is not None:
            self.stack.append(self.cur)
            self.cur = self.cur.left
        self.cur = self.stack.pop()
        res = self.cur.val
        self.cur = self.cur.right
        return res
