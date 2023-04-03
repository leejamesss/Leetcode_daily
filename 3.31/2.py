#整体思路：
#方法：递归

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        k1 = ( len(nums1) + len(nums2) + 1 ) // 2               
        k2 = ( len(nums1) + len(nums2) + 2 ) // 2                   #首先给出中位数可能用到的数字（可能位于中位的两个数）
        def helper(nums1,nums2,k):                                  #定义找到第k小的数字的函数
            if(len(nums1) <len(nums2) ):                            
                nums1, nums2 = nums2 , nums1                        #保持nums1比较长
            if(len(nums2)==0):
                return nums1[k-1]                                   # 短数组空，直接返回（两个方式共同讨论短板数组为空的情况）
            if(k==1):                                               #边界条件：k表示最小的数字
                return min(nums1[0],nums2[0])                       #找最小数，比较数组首位
            t = min(k//2,len(nums2))                                # 保证不上溢（给出k就是最小的数字）        
            if( nums1[t-1]>=nums2[t-1] ):                           # 递归调用比较num1[t-1]和nums2[t-1]的大小：t理解做指向两个列表中需要比较大小的数的指针
                return helper(nums1 , nums2[t:],k-t)                
            else:
                return helper(nums1[t:],nums2,k-t)
        return ( helper(nums1,nums2,k1) + helper(nums1,nums2,k2) ) /2
     
    
    
#后续优化：
#时间优化：二分查找
