// https://leetcode.cn/problems/valid-square/
class Solution {
    public boolean validSquare(int[] p1, int[] p2, int[] p3, int[] p4) {
        int[][] points = new int[][] {p1, p2, p3, p4};
        Set<Integer> distances = new HashSet<>();
        
        for (int i = 0; i < 4; i++) {
            for (int j = i + 1; j < 4; j++) {
                int dist = calculateDistance(points[i], points[j]);
                if (dist == 0) {
                    return false;
                }
                distances.add(dist);
            }
        }
        
        return distances.size() == 2;
    }
    
    private int calculateDistance(int[] p1, int[] p2) {
        int dx = p1[0] - p2[0];
        int dy = p1[1] - p2[1];
        return dx * dx + dy * dy;
    }
}
