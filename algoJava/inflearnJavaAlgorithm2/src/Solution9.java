// 9. 격자판 최대합
// 설명
// 5*5 격자판에 아래롸 같이 숫자가 적혀있습니다.
// 10 13 10 12 15
// 12 39 30 23 11
// 11 25 50 53 15
// 19 27 29 37 27
// 19 13 30 13 19
//
// N*N의 격자판이 주어지면 각 행의 합, 각 열의 합, 두 대각선의 합 중 가 장 큰 합을 출력합니다.
//
// 입력
// 첫 줄에 자연수 N이 주어진다.(2<=N<=50)
// 두 번째 줄부터 N줄에 걸쳐 각 줄에 N개의 자연수가 주어진다. 각 자연수는 100을 넘지 않는다.
//
// 출력
// 최대합을 출력합니다.
//
// 예시 입력 1
// 5
// 10 13 10 12 15
// 12 39 30 23 11
// 11 25 50 53 15
// 19 27 29 37 27
// 19 13 30 13 19
//
// 예시 출력 1
// 155

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
