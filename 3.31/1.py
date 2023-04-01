#滑动窗口问题
#滑动窗口思想：
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen,hashmap=0,{}                                      #初始化最大长度   和哈希表用来检验是不是唯一的字符
        left=0                                                   #初始化左指针
        for right in range(len(s)):                              #遍历右指针
            hashmap[s[right]]=hashmap.get(s[right],0)+1          #右指针纳入哈希表并且计数
            if len(hashmap)==right-left+1:                       #如果唯一，就更新maxLen
                maxLen=max(maxLen,right-left+1)                  
            while right -left+1>len(hashmap):                    #如果发现有重复字符时，则移动左端点，直到子串中所有字符都唯一为止。
                head=s[left]                                     #检查左端点指向的字符是否是重复字符
                hashmap[head]-=1                                 #向左移动带来的损失
                if hashmap[head]==0:                      
                    del hashmap[head] 
                left+=1                                          #移动左指针
        return maxLen




