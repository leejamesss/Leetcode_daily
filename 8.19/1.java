class Solution {
    public int findLHS(int[] nums) {
        Map<Integer, Integer> countMap = new HashMap<>();
        
        for (int num : nums) {
            countMap.put(num, countMap.getOrDefault(num, 0) + 1);
        }
        
        int maxLen = 0;
        
        for (int num : countMap.keySet()) {
            if (countMap.containsKey(num + 1)) {
                int len = countMap.get(num) + countMap.get(num + 1);
                maxLen = Math.max(maxLen, len);
            }
        }
        
        return maxLen;
    }
}
// https://leetcode.cn/problems/longest-harmonious-subsequence/
