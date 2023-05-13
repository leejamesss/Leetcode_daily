class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res = []
        if len(s) < 11:
            return res
        # 哈希表，key为子串，value为出现次数
        dic = {}
        # 滑动窗口
        for i in range(len(s)-9):
            sub_str = s[i:i+10]
            hash_val = hash(sub_str)
            if hash_val in dic:
                dic[hash_val] += 1
                if dic[hash_val] == 2:
                    res.append(sub_str)
            else:
                dic[hash_val] = 1
        return res
#      https://leetcode.cn/problems/repeated-dna-sequences/submissions/
