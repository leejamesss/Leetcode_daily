# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        tmp = 0
        val = 0
        head=Linkedlist = ListNode()
        while l1 or l2 or tmp:
            val=tmp
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next

            tmp = val//10
            val = val%10
            Linkedlist.next = ListNode(val)
            Linkedlist = Linkedlist.next
        return head.next
