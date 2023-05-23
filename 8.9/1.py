# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "null"
        return str(root.val)+','+self.serialize(root.left)+','+self.serialize(root.right)

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def build_tree(data_list):
            if not data_list:
                return None
            val = data_list.pop(0)
            if val =='null':
                return None
            root = TreeNode(int(val))
            root.left=build_tree(data_list)
            root.right=build_tree(data_list)
            return root
        data_list =data.split(',')
        return build_tree(data_list)

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# https://leetcode.cn/problems/serialize-and-deserialize-binary-tree/submissions/
