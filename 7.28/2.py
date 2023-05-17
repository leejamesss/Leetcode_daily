# https://leetcode.cn/problems/peeking-iterator/
class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self.peek_val = None if not iterator.hasNext() else iterator.next()

    def peek(self):
        return self.peek_val

    def next(self):
        val_to_return = self.peek_val
        self.peek_val = None if not self.iterator.hasNext() else self.iterator.next()
        return val_to_return

    def hasNext(self):
        return self.peek_val is not None
