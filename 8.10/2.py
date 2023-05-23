
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:

        stack = []
        nodes =preorder.split(',')
        for node in nodes:
            stack.append(node)
            while len(stack)>2 and stack[-2:] ==['#','#'] and stack[-3] != '#':
                stack.pop() 
                stack.pop()
                stack.pop()
                stack.append('#')

        return len(stack) ==1 and stack[0] =='#'
# https://leetcode.cn/problems/verify-preorder-serialization-of-a-binary-tree/
