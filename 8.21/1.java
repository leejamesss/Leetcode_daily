import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public String[] findRestaurant(String[] list1, String[] list2) {
        Map<String, Integer> map = new HashMap<>();
        List<String> result = new ArrayList<>();
        int minIndexSum = Integer.MAX_VALUE;

        for (int i = 0; i < list1.length; i++) {
            map.put(list1[i], i);
        }

        for (int j = 0; j < list2.length; j++) {
            if (map.containsKey(list2[j])) {
                int indexSum = j + map.get(list2[j]);
                if (indexSum < minIndexSum) {
                    result.clear();
                    result.add(list2[j]);
                    minIndexSum = indexSum;
                } else if (indexSum == minIndexSum) {
                    result.add(list2[j]);
                }
            }
        }

        return result.toArray(new String[result.size()]);
    }
}
https://leetcode.cn/problems/minimum-index-sum-of-two-lists/
