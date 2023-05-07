# https://leetcode.cn/problems/reorder-list/submissions/

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        
        # 快慢指针找到链表中点
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # 将链表从中点断开，并反转右半部分
        prev, curr = None, slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        
        # 将左半部分和反转后的右半部分交替合并
        p1, p2 = head, prev
        while p2.next:
            p1.next, p1 = p2, p1.next
            p2.next, p2 = p1, p2.next
