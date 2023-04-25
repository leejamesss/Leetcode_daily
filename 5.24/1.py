# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# https://leetcode.cn/problems/convert-sorted-list-to-binary-search-tree/submissions/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            # 链表为空，返回 None
            return None
        
        if not head.next:
            # 链表只有一个节点，直接构造该节点
            return TreeNode(head.val)
        
        # 快慢指针找到链表的中间节点
        slow, fast = head, head.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # 构造根节点
        root = TreeNode(slow.next.val)
        
        # 分别递归构造左子树和右子树
        right_head = slow.next.next
        slow.next = None
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(right_head)
        
        return root
