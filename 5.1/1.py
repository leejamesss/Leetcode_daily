#https://leetcode.cn/problems/add-binary/submissions/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n=int(a,2)+int(b,2)
        bin_string = bin(n)[2:]  # 将整数n转换为二进制，并去掉前缀"0b"
        return bin_string
        
