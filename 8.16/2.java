import java.util.Random;

class Solution {
    private double radius;
    private double xCenter;
    private double yCenter;
    private Random random;

    public Solution(double radius, double xCenter, double yCenter) {
        this.radius = radius;
        this.xCenter = xCenter;
        this.yCenter = yCenter;
        this.random = new Random();
    }

    public double[] randPoint() {
        double r = Math.sqrt(random.nextDouble()) * radius; // 生成0到半径的随机距离
        double angle = random.nextDouble() * 2 * Math.PI; // 生成0到2π的随机角度

        double x = r * Math.cos(angle) + xCenter; // 极坐标转换为直角坐标
        double y = r * Math.sin(angle) + yCenter;

        return new double[]{x, y};
    }
}
// https://leetcode.cn/problems/generate-random-point-in-a-circle/submissions/
