// https://leetcode.cn/problems/find-k-pairs-with-smallest-sums/submissions/
import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;

class Solution {
    public List<List<Integer>> kSmallestPairs(int[] nums1, int[] nums2, int k) {
        List<List<Integer>> result = new ArrayList<>();
        
        // 创建一个最小堆，用于保存数字对的和
        PriorityQueue<int[]> queue = new PriorityQueue<>((a, b) -> (a[0] + a[1]) - (b[0] + b[1]));
        
        // 将所有满足条件的数字对加入最小堆
        for (int i = 0; i < nums1.length && i < k; i++) {
            queue.offer(new int[]{nums1[i], nums2[0], 0});            
        }
        
        // 从最小堆中取出和最小的数字对，直到取出了 k 个数字对或者堆为空
        while (k-- > 0 && !queue.isEmpty()) {
            int[] cur = queue.poll();
            int num1 = cur[0];
            int num2 = cur[1];
            int index2 = cur[2];
            result.add(List.of(num1, num2));
            
            // 如果当前数字对来自 nums1 的元素还有下一个元素，则将下一个数字对加入最小堆
            if (index2 + 1 < nums2.length) {
                queue.offer(new int[]{num1, nums2[index2 + 1], index2 + 1});
            }
        }
        
        return result;
    }
}
