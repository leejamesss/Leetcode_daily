class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = []  # 入栈队列
        self.queue2 = []  # 出栈队列

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue1.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        # 把 queue1 中的元素依次出队并加入到 queue2 中，直到只剩下一个元素
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.pop(0))
        # 将 queue1 中最后一个元素弹出作为栈顶元素
        res = self.queue1.pop(0)
        # 交换 queue1 和 queue2 的引用
        self.queue1, self.queue2 = self.queue2, self.queue1
        return res

    def top(self) -> int:
        """
        Get the top element.
        """
        # 把 queue1 中的元素依次出队并加入到 queue2 中，直到只剩下一个元素
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.pop(0))
        # 将 queue1 中最后一个元素弹出并返回作为栈顶元素
        res = self.queue1.pop(0)
        # 把该元素加入到 queue2 中
        self.queue2.append(res)
        # 交换 queue1 和 queue2 的引用
        self.queue1, self.queue2 = self.queue2, self.queue1
        return res

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.queue1) == 0
# https://leetcode.cn/problems/implement-stack-using-queues/submissions/
