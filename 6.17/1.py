# https://leetcode.cn/problems/intersection-of-two-linked-lists/submissions/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
       
        # 遍历链表获取长度
        lenA, lenB = 0, 0
        curA, curB = headA, headB
        while curA:
            lenA += 1
            curA = curA.next
        while curB:
            lenB += 1
            curB = curB.next

        # 如果尾节点不同，说明两个链表不相交
        if curA != curB:
            return None

        # 让长的链表先走多出来的步数
        curA, curB = headA, headB
        if lenA > lenB:
            for _ in range(lenA - lenB):
                curA = curA.next
        else:
            for _ in range(lenB - lenA):
                curB = curB.next

        # 让两个链表同时向后遍历，直到找到相交的节点为止
        while curA != curB:
            curA = curA.next
            curB = curB.next

        return curA

        
