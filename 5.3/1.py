class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for dir in path.split('/'):
            if dir == '.' or not dir:
                # 当 dir 为 '.' 或者 '' (即连续斜杠) 时，不改变当前路径
                continue
            elif dir == '..':
                # 当 dir 为 '..' 时，返回上一级目录
                if stack:
                    stack.pop()
            else:
                # 当 dir 为其他字符串时，将其加入路径
                stack.append(dir)
        return '/' + '/'.join(stack)
