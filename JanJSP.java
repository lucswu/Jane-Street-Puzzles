public class JanJSP {
	public int[][][][] ans;

	public static void main (String[] args) {
		int[][] ans = new int[1000][1000][1000][1000];
		int max = 0;
		int maxSum = 0;
		maxI = 0;
		maxJ = 0;
		maxK = 0;
		maxL = 0;
		for (int i = 0; i < 1000; i++) {
			for (int j = 0; j < 1000; j++) {
				for (int k = 0; k < 1000; k++) {
					for (int l = 0; l < 1000; l++) {
						helper(i, j, k, l);
						if (ans[i][j][k][l] > max) {
							max = Math.max(ans[i][j][k][l]);
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

	public static void helper(int i, int j, int k, int l) {
		if (i == 0 && j == 0 && k == 0 && l == 0) return 0;
		if (ans[i][j][k][l] > 0) {
			return ans[i][j][k][l];
		}
		return 1 + helper(Math.abs(i - j), Math.abs(j -  k), Math.abs(k - l), Math.abs(l - i));
	}

}
