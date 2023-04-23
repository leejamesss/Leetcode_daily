#https://leetcode.cn/problems/partition-list/submissions/
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        small_head = ListNode(0)
        big_head = ListNode(0)
        small = small_head
        big = big_head
        while head:
            if head.val < x:
                small.next = head
                small = small.next
            else:
                big.next = head
                big = big.next
            head = head.next
        # 将两个链表拼接起来
        big.next = None
        small.next = big_head.next
        return small_head.next
