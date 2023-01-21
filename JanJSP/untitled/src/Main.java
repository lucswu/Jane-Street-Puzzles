public class Main {
    public static int[][][][] ans;
    public static final int num = 210;

//    public static void main (String[] args) {
//        ans = new int[num][num][num][num];
//        for (int i = 1; i < num; i++) {
//            System.out.println("\ni: " + i);
//            iter(i);
//
//        }
//    }

    public static void main (String[] args) {
        int largest = 0;
        int lastStart = 0;
        int power = 3;
        while (largest < 10000000) {
            int a = 0;
            int b = (int) Math.pow(2, power);
            int c = 2 * (int) Math.pow(2, power);
            int d = 3 * (int) Math.pow(2, power);
            int iterations = 5;
            while ((c - a) % 2 == 0) {
                int a1 = (c - a) / 2;
                int a2 = a1 + a;
                int a3 = a2 + b;
                int a4 = a3 + c;
                a = a1;
                b = a2;
                c = a3;
                d = a4;
                iterations++;
                System.out.println(a + " " + b + " " + c + " " + d);
            }
            System.out.println(iterations);
            System.out.println();
            largest = d;
            lastStart = power - 1;
            power++;
        }
        System.out.println("\n" + lastStart);
    }

    public static void iter (int n) {
        int max = 0;
        int maxSum = 0;
        int maxI = 0;
        int maxJ = 0;
        int maxK = 0;
        int maxL = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                for (int k = 0; k < n; k++) {
                    for (int l = 0; l < n; l++) {
                        ans[i][j][k][l] = helper(i, j, k, l);
                        if (ans[i][j][k][l] > max) {
                            max = ans[i][j][k][l];
                            maxSum = i + j + k + l;
                            maxI = i;
                            maxJ = j;
                            maxK = k;
                            maxL = l;
                        }
                        if (ans[i][j][k][l] == max && maxSum > i + j + k + l) {
                            maxSum = i + j + k + l;
                            maxI = i;
                            maxJ = j;
                            maxK = k;
                            maxL = l;
                        }
                    }
                }
            }
        }
        System.out.println(maxI);
        System.out.println(maxJ);
        System.out.println(maxK);
        System.out.println(maxL);
        System.out.println("max: " + max);
    }

    public static int helper(int i, int j, int k, int l) {
        if (i == 0 && j == 0 && k == 0 && l == 0) return 0;
        if (ans[i][j][k][l] > 0) {
            return ans[i][j][k][l];
        }
        return 1 + helper(Math.abs(i - j), Math.abs(j -  k), Math.abs(k - l), Math.abs(l - i));
    }

}
