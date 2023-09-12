https://leetcode.cn/problems/design-hashmap/description/
class MyHashMap {
    private final int size = 1000001;
    private final int[] map;

    public MyHashMap() {
        map = new int[size];
        Arrays.fill(map, -1);
    }

    public void put(int key, int value) {
        map[key] = value;
    }

    public int get(int key) {
        return map[key];
    }

    public void remove(int key) {
        map[key] = -1;
    }
}
