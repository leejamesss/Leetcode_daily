

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next
# https://leetcode.cn/problems/delete-node-in-a-linked-list/submissions/
