
# https://leetcode.cn/problems/restore-ip-addresses/submissions/
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        def backtracking(start: int, path: List[str]):
            if len(path) == 4 and start == len(s):
                res.append('.'.join(path))
                return
            
            if len(path) == 4 or start == len(s):
                return
            
            for i in range(1, 4):
                if start + i > len(s):
                    break
                
                segment = s[start:start+i]
                if (len(segment) > 1 and segment.startswith('0')) or int(segment) > 255:
                    continue
                
                path.append(segment)
                backtracking(start + i, path)
                path.pop()
        
        backtracking(0, [])
        return res
