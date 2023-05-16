class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []  # 栈1用于入队列
        self.stack2 = []  # 栈2用于出队列

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.stack2:  # 如果栈2为空，将栈1中的元素弹出并压入栈2
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()  # 返回栈2的栈顶元素

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.stack2:  # 如果栈2为空，将栈1中的元素弹出并压入栈2
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]  # 返回栈2的栈顶元素，但不弹出

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.stack1 and not self.stack2
# https://leetcode.cn/problems/implement-queue-using-stacks/submissions/
