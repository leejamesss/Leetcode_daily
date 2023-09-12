

class Solution {
    public List<String> topKFrequent(String[] words, int k) {
        // 统计每个单词的出现次数
        Map<String, Integer> map = new HashMap<>();
        for (String word : words) {
            map.put(word, map.getOrDefault(word, 0) + 1);
        }
        // 将单词和对应的出现次数存储到List中
        List<String> list = new ArrayList<>(map.keySet());
        // 按出现次数和字典顺序排序
        Collections.sort(list, new Comparator<String>() {
            @Override
            public int compare(String word1, String word2) {
                int count1 = map.get(word1);
                int count2 = map.get(word2);
                if (count1 != count2) {
                    return count2 - count1;
                } else {
                    return word1.compareTo(word2);
                }
            }
        });
        // 取前k个单词
        return list.subList(0, k);
    }
}
https://leetcode.cn/problems/top-k-frequent-words/
