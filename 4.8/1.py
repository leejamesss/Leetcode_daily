
# https://leetcode.cn/problems/merge-two-sorted-lists/
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        elif not l2:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
#递归
#一个链表为空，直接返回另一个链表
#否则，比较两个链表的头节点，将较小的节点作为新的头节点，递归调用 merge 函数合并剩下的部分
