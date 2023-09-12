class MapSum {
    
    class TrieNode {
        TrieNode[] children;
        int value;
        
        public TrieNode() {
            children = new TrieNode[26];
            value = 0;
        }
    }
    
    private TrieNode root;

    /** Initialize your data structure here. */
    public MapSum() {
        root = new TrieNode();
    }
    
    public void insert(String key, int val) {
        TrieNode node = root;
        for (char c : key.toCharArray()) {
            int index = c - 'a';
            if (node.children[index] == null) {
                node.children[index] = new TrieNode();
            }
            node = node.children[index];
        }
        node.value = val;
    }
    
    public int sum(String prefix) {
        TrieNode node = root;
        for (char c : prefix.toCharArray()) {
            int index = c - 'a';
            if (node.children[index] == null) {
                return 0;
            }
            node = node.children[index];
        }
        return dfs(node);
    }
    
    private int dfs(TrieNode node) {
        int sum = node.value;
        for (TrieNode child : node.children) {
            if (child != null) {
                sum += dfs(child);
            }
        }
        return sum;
    }
}
https://leetcode.cn/problems/map-sum-pairs/
