import java.util.Scanner;

public class Solution7 {

    static int[][] ch;

    public int solution(int n, int r) {

        if (ch[n][r] != 0) {
            return ch[n][r];
        }

        if (n == r || r == 0) {
            return 1;
        }

        return ch[n][r] = solution(n - 1, r - 1) + solution(n - 1, r);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int r = scanner.nextInt();

        ch = new int[n+1][r+1];

        Solution7 solution7 = new Solution7();
        System.out.println(solution7.solution(n, r));
    }

}
