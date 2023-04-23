#https://leetcode.cn/problems/remove-duplicates-from-sorted-list-ii/submissions/
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # 如果链表为空或者只有一个节点，则直接返回原链表
        if not head or not head.next:
            return head
        
        # 如果当前节点和下一个节点值相同，则一直向后移动指针
        if head.val == head.next.val:
            while head.next and head.val == head.next.val:
                head = head.next
            return self.deleteDuplicates(head.next) # 返回删除后剩下的节点
        else:
            head.next = self.deleteDuplicates(head.next) # 否则，继续递归处理下一个节点
            return head
