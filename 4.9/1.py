
# https://leetcode.cn/problems/merge-k-sorted-lists/
#分治思想
#两两合并
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        n = len(lists)
        return self.mergeKListsRange(lists, 0, n - 1)
    
    def mergeKListsRange(self, lists, left, right):
        if left == right:
            return lists[left]
        mid = left + (right - left) // 2
        l1 = self.mergeKListsRange(lists, left, mid)
        l2 = self.mergeKListsRange(lists, mid + 1, right)
        return self.mergeTwoLists(l1, l2)
    
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
