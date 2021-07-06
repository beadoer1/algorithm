import java.util.Scanner;

public class Solution9 {

    public int solution(int n, int[][] arr) {
        // my answer (164ms) 이게 더 빠른데 코드는 더 복잡하다. 뭐가 더 좋은 답일까..
//        int maxSum = 0;
//        int sum = 0;
//
//        for (int i = 0; i < n; i++) {
//            // 행 기준 최대값
//            sum = 0;
//            for (int j = 0; j < n; j++) {
//                sum += arr[i][j];
//            }
//            if(sum > maxSum){
//                maxSum = sum;
//            }
//
//            // 열 기준 최대값
//            sum = 0;
//            for (int j = 0; j < n; j++) {
//                sum += arr[j][i];
//            }
//            if(sum > maxSum){
//                maxSum = sum;
//            }
//        }
//        // 대각선 최대값(순방향)
//        sum = 0;
//        for (int i = 0; i < n; i++) {
//            sum += arr[i][i];
//        }
//        if(sum > maxSum){
//            maxSum = sum;
//        }
//        // 대각선 최대값(역방향)
//        sum = 0;
//        for (int i = 0; i < n; i++) {
//            sum += arr[i][n-1-i];
//        }
//        if(sum > maxSum){
//            maxSum = sum;
//        }
//
//        return maxSum;

        //lecture answer (173ms)
        int maxSum = 0;
        int sum1, sum2;

        for (int i = 0; i < n; i++) {
            // 행 기준 최대값
            sum1 = sum2 = 0;
            for (int j = 0; j < n; j++) {
                sum1 += arr[i][j];
                sum2 += arr[j][i];
            }
            maxSum = Math.max(maxSum, sum1);
            maxSum = Math.max(maxSum, sum2);
        }
        // 대각선 최대값(순방향)
        sum1 = sum2 = 0;
        for (int i = 0; i < n; i++) {
            sum1 += arr[i][i];
            sum2 += arr[i][n - i - 1];
        }
        maxSum = Math.max(maxSum, sum1);
        maxSum = Math.max(maxSum, sum2);

        return maxSum;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();

        int[][] arr = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                arr[i][j] = scanner.nextInt();
            }
        }

        Solution9 solution9 = new Solution9();
        System.out.println(solution9.solution(n, arr));
    }
}
